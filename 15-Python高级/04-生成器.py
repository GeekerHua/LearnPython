#!/usr/bin/env python
# coding=utf-8

'''
# Author = GeekerHua
# 2017.02.08 17:16:25
'''

# 创建生成器

L = [x * 2 for x in range(5)]
print(L)

G = (x * 2 for x in range(5))
print(G)

print(next(G))
print(next(G))
print(next(G))
print(next(G))


# 斐波拉契数列（Fibonacci)
def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1
    # return "done"


F = fib(5)
print('---')
next(F)
next(F)
next(F)
next(F)
next(F)
