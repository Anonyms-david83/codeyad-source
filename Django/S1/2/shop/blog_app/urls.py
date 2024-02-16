from django.urls import path
from . import views

urlpatterns = [
    path('home' , views.home)   #this url is now connected to the home function
]

#this urls are connected to the main urls with inclued function in urls.py in the main project