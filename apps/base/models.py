from django.db import models


# Create your models here.

class Info(models.Model):
    name = models.CharField(verbose_name='测试', max_length=32)
