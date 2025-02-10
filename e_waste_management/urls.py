from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('learnmore',views.learnmore,name='learnmore'),
    path('pickup',views.pickup,name='pickup'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('contactus', views.contactus,name='contactus'),
    path('resetpassword', views.resetpassword,name='resetpassword'),
    path('track', views.track,name='track')


]