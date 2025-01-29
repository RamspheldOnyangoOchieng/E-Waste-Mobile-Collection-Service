# e_waste_management/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Home page view
def home(request):
    # This will render a template called 'home.html'
    return render(request, 'home.html')

# Learn more page view
def learnmore(request):
    # This will render a template called 'learnmore.html'
    return render(request, 'learnmore.html')

# Login view
def login_view(request):
    # This will render a template called 'login.html'
    if request.method == 'POST':
        # Handle login form submission
        # For example, you can authenticate the user here
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate logic goes here...
        return HttpResponse("Login successful")  # Placeholder for login logic
    return render(request, 'login.html')

# Register view
def register_view(request):
    # This will render a template called 'register.html'
    if request.method == 'POST':
        # Handle registration form submission
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Register logic goes here...
        return HttpResponse("Registration successful")  # Placeholder for register logic
    return render(request, 'register.html')

# Contact us view
def contactus(request):
    # This will render a template called 'contactus.html'
    return render(request, 'contactus.html')
