from django.contrib import admin
from .models import Order, Product


class OrderAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)

admin.site.register(Product, ProductAdmin)
