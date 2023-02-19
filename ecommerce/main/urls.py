from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('username', views.get_username),
    path('products', views.get_products),
    # path('create-post', views.create_post, name='create_post'),
]