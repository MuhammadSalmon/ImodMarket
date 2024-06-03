from django.urls import path, include
from .views import ProductListView, ProductDetailsView, ProductUpdateView, MyView
app_name = "shopapp"
urlpatterns = [
    # path('home/', MyView.as_view(), name='home'),
    path('', MyView.as_view(), name='home'),
    path('product/', ProductListView.as_view(), name='product'),
    path('product_detail/<int:pk>', ProductDetailsView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='product_list'),
]



    # path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
