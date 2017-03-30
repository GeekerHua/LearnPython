# coding=utf-8
from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    atitle = models.CharField(verbose_name='地区名称', max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle.encode('utf-8')

    def title(self):
        return self.atitle.encode('utf-8')

    title.admin_order_field = 'atitle'
    title.short_description = '地区名称2'


class picTest(models.Model):
    pic = models.ImageField(upload_to='booktest/')
