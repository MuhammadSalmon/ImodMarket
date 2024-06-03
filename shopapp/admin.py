from django.contrib import admin

# Register your models here.
from .models import Product

# class ProductItem(admin.TabularInline):
#     model = Product

# class CartAdmin(admin.ModelAdmin):
#     inlines = [ProductItem]

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem

# class OrderAdmin(admin.ModelAdmin):
#     inlines = [OrderItemInline]

# admin.site.register(Cart, CartAdmin)
# admin.site.register(Order, OrderAdmin)
# # # Register your models here.

admin.site.register(Product)
# # admin.site.register(Order)
# admin.site.register(OrderItem)