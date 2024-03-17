from django.urls import path
from . import views

urlpatterns = [
    # USER URLS
    path('home/', views.home, name="home"),
    path('user_header/', views.home, name="user_header"),
    path('menu/', views.menu, name='menu'),
    path('product/', views.product, name='product'),
    path('user_cart/', views.user_cart, name='user_cart'),
    path('user_checkout/', views.user_checkout, name='user_checkout'),
    path('about/', views.about, name='about'),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),

    # ADMIN URLS
    path('admin_index/', views.admin_index, name='admin_index'),
]