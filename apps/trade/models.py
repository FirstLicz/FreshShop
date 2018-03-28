from django.db import models
from django.contrib.auth import get_user_model

#User = get_user_model()
#User等价于from users.models import UserProfile
from goods.models import Goods


from datetime import datetime


User = get_user_model()

# Create your models here.


class ShoppingCart(models.Model):
    '''
        购物车
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品')
    nums = models.IntegerField(default=0,verbose_name='购买数量')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural =verbose_name

    def __str__(self):
        return '%s(%d)' %(self.goods.name,self.nums)


class OrderInfo(models.Model):
    '''
        订单
    '''
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付"),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    order_sn = models.CharField(max_length=30,verbose_name='订单号')
    trade_no = models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name='交易号')
    pay_status = models.CharField(max_length=30,choices=ORDER_STATUS,default='paying',verbose_name='交易状态')
    post_message = models.CharField(max_length=100,verbose_name='订单留言',null=True,blank=True)
    order_mount = models.FloatField(default=0.0,verbose_name='交易金额')
    pay_time = models.DateTimeField(null=True,blank=True,verbose_name='支付时间')

    #用户信息
    address = models.CharField(max_length=200,verbose_name='订单地址',default='')
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    '''
        订单里的商品详情
    '''
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE,verbose_name='订单详情')
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品')
    goods_nums = models.IntegerField(default=0,verbose_name='商品的数量')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)







