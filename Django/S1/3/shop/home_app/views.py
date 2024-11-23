from django.shortcuts import render , HttpResponse


def home(request):
    return HttpResponse('hi this is the homepage')


def contactus(request):
    return HttpResponse('hi this is the contactus page')