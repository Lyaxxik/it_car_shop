from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def sedan_page(request):
    return render(request, 'main/sedan.html', {})

def crossover_page(request):
    return render(request, 'main/crossover.html', {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(reverse('main:profile_page', args=()))
        else:
            return redirect(reverse('main:login_page', args=()))
    return render(request, 'main/login.html', {})

def profile_page(request):
    if request.user.is_authenticated:
        return render(request, 'main/profile_page.html', {})
    else:
        return redirect(reverse('main:login_page', args=()))

def logout_view(request):
    logout(request)
    return redirect(reverse('main:index_page', args=()))

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=firstname,
            last_name=lastname,
        )
        user.set_password(password)
        user.save()
        return redirect(reverse('main:login_page', args=()))
    return render(request, 'main/register.html', {})
