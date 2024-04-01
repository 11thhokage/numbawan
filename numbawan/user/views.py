from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Profile
from .forms import RegisterForm, LoginForm


# AUTH
def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid login credentials.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                profile_data = {
                    k: v
                    for k, v in form.cleaned_data.items()
                    if k in Profile._meta.get_fields()
                }
                profile = Profile(user=user, **profile_data)
                profile.save()
                user_exists = User.objects.filter(email=user.email).exists()
                if user_exists:
                    messages.success(
                        "User successfully registered and saved in the database."
                    )
                    return redirect("login")
                else:
                    messages.error("User registration failed.")
            except IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    messages.error(request, "User already exists.")
                else:
                    messages.error(request, "An error occurred while registering.")
                return render(request, "register.html", {"form": form})
        else:
            messages.error(request, f"Invalid input: {form.errors}")

    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# STORE
def home(request):
    return render(request, "home.html")


def user_header(request):
    return render(request, "user_header.html")


def menu(request):
    return render(request, "menu.html")


def product(request):
    return render(request, "product.html")


def user_cart(request):
    return render(request, "user_cart.html")


def user_checkout(request):
    return render(request, "user_checkout.html")


def about(request):
    return render(request, "about.html")


# ADMIN
def admin_index(request):
    return render(request, "admin_index.html")


def admin_acc_management(request):
    return render(request, "admin_acc_management.html")


def admin_category(request):
    return render(request, "admin_category.html")


def admin_product(request):
    return render(request, "admin_product.html")


def admin_order(request):
    return render(request, "admin_order.html")


def admin_view_order(request):
    return render(request, "admin_view_order.html")
