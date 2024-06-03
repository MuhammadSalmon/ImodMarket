from django.urls import path
from .views import AddToCartView, CartDetailView, CheckoutView, OrderConfirmationView

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-confirmation/<int:order_id>/', OrderConfirmationView.as_view(), name='order_confirmation'),
]