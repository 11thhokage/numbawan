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
    path('admin_acc_management/', views.admin_acc_management, name='admin_acc_management'),
    path('admin_category/', views.admin_category, name='admin_category'),
    path('admin_product/', views.admin_product, name='admin_product'),
    path('admin_order/', views.admin_order, name='admin_order'),
    path('admin_view_order/', views.admin_view_order, name='admin_view_order'),
]