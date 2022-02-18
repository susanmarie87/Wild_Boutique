"""Admin file reads metadata from models"""
from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """Displays Product details"""
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    """Displays product friendly name"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
