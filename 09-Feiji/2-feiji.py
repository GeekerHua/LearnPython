#./usr/bin/env python3
#coding=utf-8

import pygame
import random
from pygame.locals import *

SCREEN_HEIGHT = 667
SCREEN_WIDTH = 375


class EnemyManager(object):
    __instance = None
    __first_init = True

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__first_init:
            self.enemyList = []
            EnemyManager.__first_init = False

    # 随机生成敌机
    def newEnemy(self):
        enemyPlane = EnemyPlane(screen, "./feiji/enemy-1.gif")
        self.enemyList.append(enemyPlane)

    def randomNewEnemy(self):
        ranInt = random.randint(0, 50)
        if ranInt %50 == 0:
            self.newEnemy()

    def displayEnemys(self, screen):
        for enemyPlane in self.enemyList:
            if enemyPlane.y > SCREEN_HEIGHT:
                self.enemyList.remove(enemyPlane)
                del enemyPlane
            else:
                enemyPlane.goDown()
                enemyPlane.display()
                # 敌机发子弹
                enemyPlane.shootBullet()
                enemyPlane.displayBullet()
                # 敌机闲逛
                enemyPlane.hangOut()


class Bullet(object):

    '''子弹类'''
    def __init__(self, x, y, screen, mine):
        self.x = x
        self.y = y
        self.mine = mine
        if mine:
            self.speed = 6
            self.image = pygame.image.load("./feiji/bullet-3.gif").convert()
        else:
            self.speed = 4
            self.image = pygame.image.load("./feiji/bullet-1.gif").convert()

        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fly(self):
        if self.mine:
            self.y -= self.speed
        else:
            self.y += self.speed
            # 计算子弹与敌机的距离


class Plane(object):
    '''飞机的父类'''
    def __init__(self, screen, picName):
        self.x = 140
        self.y = SCREEN_HEIGHT - 140
        self.image = pygame.image.load(picName).convert()
        self.speed = 10
        self.bulletList = []
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def moveLeft(self):
        self.x -= self.speed

    def moveRight(self):
        self.x += self.speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

    def shootBullet(self):
        bullet =  Bullet(self.x + 40, self.y - 20, self.screen, True)
        self.bulletList.append(bullet)
        print("我的子弹个数为%d"%len(self.bulletList))

    def displayBullet(self):
        for bullet in self.bulletList:
            bullet.fly()
            self.testDistance(bullet)
            bullet.display()
            if bullet != None and bullet.y < -10:
                self.bulletList.remove(bullet)
                del bullet

    def testDistance(self, bullet):
        enemyManager = EnemyManager()
        for enemyPlane in enemyManager.enemyList:
            print("x = %d,y = %d"%(bullet.x, bullet.y))
            distance = ((bullet.x - enemyPlane.x)**2 + (bullet.y - enemyPlane.y)**2)
            print(distance)
            if distance < 800:
                print("**************飞机被射中了****************")
                enemyManager.enemyList.remove(enemyPlane)
                del enemyPlane
                if bullet in self.bulletList:
                    self.bulletList.remove(bullet)


class EnemyPlane(Plane):

    def __init__(self, screen, picName):
        super().__init__(screen, picName)
        self.y = 20
        self.moveSpeed = random.randint(1,5)
        self.goDownSpeed = random.randint(1,4)
        self.direction = 'right'

    def shootBullet(self):
        # 随机发子弹

        ranInt = random.randint(0,200)
        if ranInt == 200:
            bullet =  Bullet(self.x + 23, self.y + 30, self.screen, False)
            self.bulletList.append(bullet)

    def displayBullet(self):
        for bullet in self.bulletList:
            bullet.fly()
            bullet.display()
            if bullet.y > SCREEN_HEIGHT :
                self.bulletList.remove(bullet)
                del bullet

    def hangOut(self):
        if self.direction == "right":
            if self.x < SCREEN_WIDTH - 80:
                self.x += self.moveSpeed
            else:
                self.direction = 'left'
        else:
            if self.x > 20:
                self.x -= self.moveSpeed
            else:
                self.direction = 'right'

    def goDown(self):
        self.y += self.goDownSpeed



if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
    background = pygame.image.load("./feiji/background.png").convert()
    heroPlane = Plane(screen, "./feiji/hero.gif")

    # 显示敌军
    enemyPlane = EnemyPlane(screen, "./feiji/enemy-1.gif")
    enemyManager = EnemyManager()
    while True:
        screen.blit(background,(0,0))
        # 显示我的子弹
        heroPlane.displayBullet()

        # 敌军生成器
        enemyManager.randomNewEnemy()
        enemyManager.displayEnemys(screen)


        # 显示敌机
        enemyPlane.display()
        # 敌机发子弹
        enemyPlane.shootBullet()
        enemyPlane.displayBullet()
        # 敌机闲逛
        enemyPlane.hangOut()

        # 显示自己的飞机
        heroPlane.display()

        for event in pygame.event.get():
            if event.type  == QUIT:
                print('exit')
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    heroPlane.moveLeft()
                elif event.key == K_d or event.key == K_RIGHT:
                    heroPlane.moveRight()
                elif event.key == K_s or event.key == K_DOWN:
                    heroPlane.moveDown()
                elif event.key == K_w or event.key == K_UP:
                    heroPlane.moveUp()
                elif event.key == K_SPACE:
                    heroPlane.shootBullet()
                print("我的飞机坐标为(%d,%d)"%(heroPlane.x, heroPlane.y))
            #else:
                #print(event)
        pygame.display.update()
