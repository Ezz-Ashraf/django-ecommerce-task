from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('username', views.get_username),
    path('products', views.get_products),
    path('logout', views.log_out),
    path('login', views.log_in),
    path('add-to-cart', views.add_to_cart),
    path('create-order', views.log_in),
    path('get-orders', views.log_in),
    path('get-cart', views.log_in),
]