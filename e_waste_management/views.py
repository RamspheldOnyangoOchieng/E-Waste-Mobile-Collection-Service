from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

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