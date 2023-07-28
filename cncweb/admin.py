from django.contrib import admin
from .models import Product, Collection, ProductImage

class ProductImageInline(admin.TabularInline): 
    model = ProductImage
    extra = 1  # Default olarak kaç tane boş form olacağını belirler

class ProductAdmin(admin.ModelAdmin): 
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)  # Özelleştirilmiş admin ile Product'ı kayıt ettik
admin.site.register(Collection)
