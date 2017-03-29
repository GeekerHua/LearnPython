# coding=utf-8
from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    def get_queryset(self):
        # 更改原始询机合
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

# 使用Manager进行创建对象
    def create_book(self, btitle, bpub_date, bread, bcommet):
        book = self.model()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # book.save()
        return book


# 定义模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=10)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    #  自定义Manager,默认管理器是objects，自定义Manager可以实现自己方法
    books = BookInfoManager()
    objects = models.Manager()

    def __str__(self):
        return self.btitle.encode('utf-8')

    # 元数据，用来自定义表名，默认为"模块名_表名"
    class Meta():
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return (self.hname + "----" + self.hcontent).encode('utf-8')
