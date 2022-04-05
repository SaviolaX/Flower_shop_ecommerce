from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug": ("category_name",)}
    list_display = ('category_name', 'category_slug', 'category_image')
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"product_slug": ("product_name",)}
    list_display = ('product_name', 'product_slug', 'product_price', 'product_category', 'product_created')
    list_editable = ['product_price']
    