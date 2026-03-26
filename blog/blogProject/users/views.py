from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'User already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('/users/login/')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

        login(request, user)
        return redirect('/')   # goes to home page

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('/users/login/')