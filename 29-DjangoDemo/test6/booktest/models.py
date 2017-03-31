from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class GoodsInfo(models.Model):
    gdesc = HTMLField()
    def __str__(self):
        return self.gdesc.encode('utf-8')


