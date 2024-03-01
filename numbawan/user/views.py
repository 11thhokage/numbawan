from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home.html")

def menu(request):
    return render(request, 'menu.html')

def product(request):
    return render(request, 'product.html')

def add_to_cart(request):
    return render(request, 'add_to_cart.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
