from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def learnmore(request):
    return render(request, 'learnmore.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def pickup(request):
    return render(request, 'pickup.html')

def contactus(request):
    return render(request, 'contactus.html')

def resetpassword(request):
    return render(request, 'resetpassword.html')

def track(request):
    return render(request, 'track.html')

