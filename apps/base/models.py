from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(verbose_name='测试', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=62)
