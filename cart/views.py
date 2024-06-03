from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, CartItem, Order, OrderItem
from .forms import AddToCartForm, OrderForm
from shopapp.models import Product


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.quantity += quantity
            cart_item.save()
            return redirect('cart:cart_detail')
        return redirect('cart:product_detail', product_id=product.id)

class CartDetailView(LoginRequiredMixin, View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        return render(request, 'cart/cart_details.html', {'cart': cart})

class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        form = OrderForm()
        print(form)
        return render(request, 'cart/checkout.html', {'form': form})

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            cart.items.all().delete()
            return redirect('cart:order_confirmation', order_id=order.id)
        return render(request, 'cart/checkout.html', {'form': form})

class OrderConfirmationView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order_items = order.items.all()
        for item in order_items:
            item.total_price = item.quantity * item.product.price
        
        total_cost = sum(item.total_price for item in order_items)
        
        return render(request, 'cart/order_confirmation.html', {
            'order': order,
            'order_items': order_items,
            'total_cost': total_cost,
        })
    
