from django.db import models
from django.contrib.auth.models import AbstractUser


from datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    '''
        user用户表
    '''
    name = models.CharField(verbose_name='姓名',null=True,blank=True,max_length=30)
    birthday = models.DateField(null=True,blank=True,verbose_name='生日')
    mobile = models.CharField(max_length=11,verbose_name='手机号码')
    gender = models.CharField(verbose_name='性别',choices=(('male','男'),('female','女')),max_length=6,default='male')
    email = models.EmailField(max_length=100,verbose_name='邮箱',null=True,blank=True)

    class Meta:
        verbose_name='用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    '''
        手机验证码
    '''
    code = models.CharField(max_length=10,verbose_name='验证码')
    mobile = models.CharField(max_length=11,verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='生成时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.code




