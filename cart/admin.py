from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

# Register your models here.
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone_number', 'created_at']
    inlines = [OrderItemInline]

# Registering CartItem and OrderItem directly
admin.site.register(CartItem)
admin.site.register(OrderItem)
