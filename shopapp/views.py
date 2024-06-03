from django.views.generic import ListView, TemplateView, DetailView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm
# Create your views her

class MyView(View):
    template_name = 'shopapp/home.html'

    def get(self, request, *args, **kwargs):
        # Fetching products from the database
        products = Product.objects.all()  # Assuming you want to fetch all products
        
        # Pass the products list to the template context
        context = {
            'products': products,
        }
        return render(request, self.template_name, context)

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
# only by name search
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     query = self.request.GET.get('query')
    #     if query:
    #         queryset = queryset.filter(name__icontains=query)
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = SearchForm()
    #     return context
    def get_queryset(self):
        queryset = super().get_queryset()
        form = ProductSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query) |
                    Q(price__icontains=query)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductSearchForm(self.request.GET)
        return context

class AboutView(TemplateView):
    template_name = 'shopapp/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data here if needed
        return context
    

class ProductDetailsView(DetailView):
    template_name = "shopapp/product-details.html"
    model = Product
    context_object_name = "product"

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "price", "description", "image"]
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return reverse(
            "shopapp:product_detail",
            kwargs={"pk": self.object.pk}
        )
    



    # ////////////////////////////////////Add to Cart View////////////////////////////

# class AddToCartView(LoginRequiredMixin, View):
#     def post(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#             cart_item.quantity += quantity
#             cart_item.save()
#             return redirect('cart_detail')
#         return render(request, 'shopapp/product_detail.html', {'product': product, 'form': form})
        
# # /////////////////////////////Cart Detail View//////////////////////////////
# class CartDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'shopapp/cart_detail.html'
#     context_object_name = 'cart'

#     def get_object(self):
#         cart, created = Cart.objects.get_or_create(user=self.request.user)
#         return cart
    


# # ////////////////////Checkout View///////////////////////////
# class CheckoutView(LoginRequiredMixin, FormView):
#     template_name = 'shopapp/checkout.html'
#     form_class = OrderForm

#     def form_valid(self, form):
#         cart = get_object_or_404(Cart, user=self.request.user)
#         order = form.save(commit=False)
#         order.user = self.request.user
#         order.save()
#         for item in cart.items.all():
#             OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
#         cart.items.all().delete()
#         return redirect('order_confirmation', order_id=order.id)
    
# # ///////////////////////////Order Confirmation View///////////////////////////////////////////
# class OrderConfirmationView(LoginRequiredMixin, DetailView):
#     model = Order
#     template_name = 'shopapp/order_confirmation.html'
#     context_object_name = 'order'

#     def get_object(self):
#         order_id = self.kwargs['order_id']
#         return get_object_or_404(Order, id=order_id)


# class AddToCartView(LoginRequiredMixin, View):
#     def post(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#             cart_item.quantity += quantity
#             cart_item.save()
#             return redirect('cart_detail')
#         return render(request, 'shopapp/product_detail.html', {'product': product, 'form': form})

# class CartDetailView(LoginRequiredMixin, View):
#     def get(self, request):
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         return render(request, 'shopapp/cart_detail.html', {'cart': cart})

# class CheckoutView(LoginRequiredMixin, View):
#     def get(self, request):
#         form = OrderForm()
#         return render(request, 'shopapp/checkout.html', {'form': form})

#     def post(self, request):
#         cart = get_object_or_404(Cart, user=request.user)
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.user = request.user
#             order.save()
#             for item in cart.items.all():
#                 OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
#             cart.items.all().delete()
#             return redirect('order_confirmation', order_id=order.id)
#         return render(request, 'shopapp/checkout.html', {'form': form})

# class OrderConfirmationView(LoginRequiredMixin, View):
#     def get(self, request, order_id):
#         order = get_object_or_404(Order, id=order_id)
#         return render(request, 'shopapp/order_confirmation.html', {'order': order})