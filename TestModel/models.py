from django.db import models
# models.py
# Create your models here.
# 类名代表了 数据库表的名字


class Test(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)