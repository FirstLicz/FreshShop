from django.db import models


from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.


class  GoodsCategory(models.Model):
    '''
        商品分类
    '''
    Category_type = (
        ('1', '一级类名'),
        ('2', '二级类名'),
        ('3', '三级类名'),
    )
    name = models.CharField(max_length=50,verbose_name='类别名',help_text='类别名',default='')
    code = models.CharField(default='',max_length=30,verbose_name='类别名code',help_text='类别名code')
    desc = models.CharField(default='',max_length=120,verbose_name='类别描述',help_text='类别描述')
    category_type = models.CharField(max_length=5,choices=Category_type,default='1',verbose_name='类别级别',help_text='类别级别')
    #用自己id作为的自己的外键
    parent_category = models.ForeignKey('self',null=True,blank=True,verbose_name='父类类别',on_delete=models.CASCADE,related_name='sub_cat',help_text='父类类别')
    is_table = models.BooleanField(default=False,verbose_name='是否放入首页导航')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsCategoryBrand(models.Model):
    '''
        品牌名
    '''
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类别', on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50,verbose_name='名称')
    desc = models.CharField(max_length=200,verbose_name='描述')
    image = models.ImageField(upload_to='brand/%Y/%m',verbose_name='品牌名图片路径')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '品牌名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    '''
    商品
    '''
    category = models.ForeignKey(GoodsCategory,verbose_name='商品类别',on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name='名称')
    goods_sn = models.CharField(max_length=80,verbose_name='商品编码',help_text='商品唯一货号')
    describe = models.CharField(max_length=200,verbose_name='描述',null=True,blank=True)
    goods_detail = UEditorField(verbose_name='商品详情',help_text='商品详情富文本',null=True,blank=True,width = 600, height = 300, filePath = "Goods/files/",imagePath='Goods/images/"')
    image = models.ImageField(max_length=200,verbose_name='商品展示图片',upload_to='goods/images/',help_text='商品图片路劲')
    free_shipping = models.BooleanField(verbose_name='是否免邮',default=False)
    market_price = models.FloatField(verbose_name='市场价',default=0)
    shop_price = models.FloatField(verbose_name='促销价',default=0)
    sales_volume = models.IntegerField(verbose_name='销量',default=0)
    goods_nums = models.IntegerField(verbose_name='商品数量',default=0)
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    is_new = models.BooleanField(default=False,verbose_name='是否新品')
    is_hot = models.BooleanField(default=False,verbose_name='是否热销')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsBannerImage(models.Model):
    '''
        商品展示图片
    '''
    goods = models.ForeignKey(Goods,verbose_name='商品',on_delete=models.CASCADE)
    image = models.ImageField(max_length=200,verbose_name='商品图片',upload_to='GoodsBanner/%Y/%m/',help_text='商品轮播图片路劲')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = '商品展示图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

class Banner(models.Model):
    '''
        商品轮播图
    '''
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品')
    image = models.ImageField(upload_to='banner',verbose_name='轮播图片')
    index = models.IntegerField(default=0,verbose_name='轮播顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name= '首页商品轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name