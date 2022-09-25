from django.contrib import admin
from products.models import Product, ProductCategory

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category__name']
    fields = ('name', 'description', 'price', 'category', 'created', 'modified')
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    autocomplete_fields = ['category']
    readonly_fields = ('created', 'modified')


class ProductCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    fields = ('name', 'description', 'created', 'modified')
    list_display = ('name',)
    readonly_fields = ('created', 'modified')


admin.site.register(Product, ProductAdmin)         # 註冊 Product 模型
admin.site.register(ProductCategory, ProductCategoryAdmin)    # 註冊 ProductCategory 模型


