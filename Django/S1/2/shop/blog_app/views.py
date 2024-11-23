from django.shortcuts import render , HttpResponse


def home(request):
    return HttpResponse('Hi')          #this is a function that will be called with the given url in urls.py which the app is also called with the given url in urls.py of the main project



# in urls.py of the main project we declear : 'blog' , and in the urls of the app we declear : 'home' that is connected to the home function
# so when we want to call the home app we type : localhost:8000/blog/home
# if we empty the url of the main urls.py of proejct like this : ' ' and also ' ' in home app : localhost:8000  -> it goes to home function
# if we empty the url of the app and we write 'blog' in the main urls of the project : localhost:8000/blog -> it call the home function