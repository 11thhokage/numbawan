from django.urls import path
from . import views

urlpatterns = [
    # AUTH URLS
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    
    # STORE URLS
    path('store/', views.home, name="home"),
    path('store/user_header/', views.home, name="user_header"),
    path('store/menu/', views.menu, name='menu'),
    path('store/product/', views.product, name='product'),
    path('store/user_cart/', views.user_cart, name='user_cart'),
    path('store/user_checkout/', views.user_checkout, name='user_checkout'),
    path('store/about/', views.about, name='about'),

    # ADMIN URLS
    path('admin/', views.admin_index, name='admin_index'),
    path('admin/acc_management/', views.admin_acc_management, name='admin_acc_management'),
    path('admin/category/', views.admin_category, name='admin_category'),
    path('admin/product/', views.admin_product, name='admin_product'),
    path('admin/order/', views.admin_order, name='admin_order'),
    path('admin/view_order/', views.admin_view_order, name='admin_view_order'),
]