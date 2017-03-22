# coding=utf-8
from django.db import models
"""
 this is a test
"""
# Create your models here.


class BookInfo(models.Model):
    """
        haha
    """
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        return '%s' % self.btitle.encode('utf-8')


class HeroInfo(models.Model):
    """
        haha
    """
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return '%d' % self.id
