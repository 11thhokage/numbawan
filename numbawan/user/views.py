from django.shortcuts import render
from .models import Profile
from .forms import RegisterForm

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
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user, **form.cleaned_data)
            profile.save()
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
