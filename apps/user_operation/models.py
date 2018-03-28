from django.db import models
from django.contrib.auth import get_user_model


from goods.models import Goods


from datetime import datetime

# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    '''
        用户收藏
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.user.name


class UserLeaveMessage(models.Model):
    '''
        用户留言
    '''
    MESSAGE_TYPE = (
        (1, '留言'),
        (2, '投诉'),
        (3, '询问'),
        (4, '售后'),
        (5, '求购'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    message_type = models.IntegerField(default=1,verbose_name='留言类型',choices=MESSAGE_TYPE)
    title = models.CharField(max_length=80,verbose_name='留言主题')
    content = models.TextField(max_length=500,verbose_name='留言内容')
    file = models.FileField(max_length=200,verbose_name='上传文件',upload_to='user/leave/message/%Y/')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.title


class UserAddress(models.Model):
    '''
        用户收货地址
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    district = models.CharField(verbose_name='配送区域',max_length=100)
    address = models.CharField(max_length=100,verbose_name='详细地址')
    signer_name = models.CharField(max_length=50,verbose_name='收货人')
    signer_mobile = models.CharField(max_length=11,verbose_name='收货人电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收货地址'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.signer_name

