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
    path('s_admin/', views.admin_index, name='admin_index'),
    path('s_admin/acc_management/', views.admin_acc_management, name='admin_acc_management'),
    path('s_admin/category/', views.admin_category, name='admin_category'),
    path('s_admin/product/', views.admin_product, name='admin_product'),
    path('s_admin/order/', views.admin_order, name='admin_order'),
    path('s_admin/view_order/', views.admin_view_order, name='admin_view_order'),
]