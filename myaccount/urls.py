from django.urls import path, include
from .views import register, UserLoginView, logout_view
# from .views import CustomLoginView, LogoutView, RegistrationView

app_name = 'myaccount'


urlpatterns = [

    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    # Other URL patterns for profile views
]