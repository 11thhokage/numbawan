from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('menu/', views.menu, name='menu'),
    path('product/', views.product, name='product'),
    path('add_to_cart/', views.product, name='add_to_cart'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]