from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('learnmore',views.learnmore,name='learnmore'),
    path('pickup',views.pickup,name='pickup'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('contactus', views.contactus,name='contactus')


]