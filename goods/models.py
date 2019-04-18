from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=20,verbose_name='店铺名称')
    location = models.CharField(max_length=30,verbose_name='店铺地址')
    create_date = models.DateField(verbose_name='开业时间')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    class Meta:
        db_table = 'shop'
        verbose_name_plural = '商店'
    def __str__(self):
        return self.name

class Goods(models.Model):
    choices_gender = (
        (0,'男'),
        (1,'女')
    )
    name = models.CharField(max_length=20,verbose_name='商品名称')
    brand_name = models.CharField(max_length=20,verbose_name='品牌名称')
    show_date = models.DateField(verbose_name='上市日期')
    gender = models.IntegerField(choices=choices_gender,default=0,verbose_name='性别')
    comment = models.CharField(max_length=200,null=True,blank=True,verbose_name='商品描述')
    is_show = models.BooleanField(default=True,verbose_name='是否展示')
    shop = models.ForeignKey('Shop',on_delete=models.CASCADE,verbose_name='店铺')

    class Meta:
        db_table = 'goods'
        #本来是默认的goods+s，下面这个可以修改名字
        verbose_name_plural = '商品'
    def __str__(self):
        return self.name

