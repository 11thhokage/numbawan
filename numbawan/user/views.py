from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.db import IntegrityError
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
            try:
                user = form.save()
                profile = Profile(user=user, **form.cleaned_data)
                profile.save()
                user_exists = User.objects.filter(email=user.email).exists()
                if user_exists:
                    messages.success("User successfully registered and saved in the database.")
                else:
                    messages.error("User registration failed.")
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    messages.error(request, 'User already exists.')
                else:
                    messages.error(request, 'An error occureed while registering.')
                return render(request, 'register.html', {'form': form})
        else:
            messages.error(request, f'Invalid input: {form.errors}')    
        
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
