from django.contrib import admin
from .models import Shop,Goods
# Register your models here.

# 直接使用自带的站点
# admin.site.register(Shop)
# admin.site.register(Goods)

#以表格的形式嵌入
class GoodsTabularInline(admin.TabularInline):
    #关联模型
    model = Goods

#以块状的形式显示
class GoodsStackedInline(admin.StackedInline):
    # 关联模型
    model = Goods

#为了控制修改admin站点
#使用装饰器注册
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    # pass
    inlines = [
        GoodsTabularInline
    ]
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # pass
    #选择可编辑的字段,如果嵌套的话，会在同一行显示多个字段
    # fields = ('name','gender','brand_name','show_date')
    #不选择可编辑的字段,下面是一个元组，如果选择元素的话，后面必须带个','
    # exclude = ('name','gender')
    #分组显示
    # fieldsets = (
    #
    #     ('基本信息', {
    #         'fields':('name','brand_name','shop','show_date')
    #     }),
    #     ('规格信息', {
    #         'fields': ('gender', 'comment', 'is_show'),
    #         'classes': ('collapse',)
    #     }),
    # )
    #通过列表显示
    list_display = ['name','brand_name','show_date','gender','shop','comment','is_show']
    # 设置字段为NUll的显示
    empty_value_display = '未填'
    # #设置进入编辑页的链接，默认第一列，必须和list_display搭配使用
    list_display_links = ['name','brand_name','show_date']
    # # 允许字段可以再列表页可以编辑,这里的属性不能与上面的字段名有冲突的
    list_editable = ['comment','is_show']
    # #在右侧显示过滤器,有外键的话可以使用外键名__name
    list_filter = ['name','gender','shop__name']


#设置站点标题
admin.site.site_title = '商品管理'
#设置站点头
admin.site.site_header = '商品管理系统'

#设置首页标题
admin.site.index_title = '速写专卖店'


