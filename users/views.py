from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import models

# Create your views here.
def home(request):
    return render(request, 'index.html') 

def signup(request):
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        # Retrieve the username and password from the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with the name of your desired redirect URL
        else:
            # If authentication fails, send an error message
            messages.error(request, "Username or password is incorrect")
            return redirect('login')  # Redirect back to the login page

    return render(request, 'login.html')  # Render the login page for GET requests


def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password =request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email = email,
            password = password 

        ) 

        user.save

        return redirect('login')
    return render(request, 'signup.html')

   


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')    
