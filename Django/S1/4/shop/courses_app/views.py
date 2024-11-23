from django.shortcuts import render , redirect
from .models import Course

def courses_list(request):
    list = Course.objects.all() #objects.all returns all the items in database : watch out it returns everything and it uses soo many resources from cpu
    return render(request , 'courses_app/courses_list.html' , context={'courses_list' : list} )


def course_detail(request , course_id):
    course = Course.objects.get(id = course_id) #objects.get : gets an object by the given argument like the id of the object
    course.views +=1 #we add a number to the views !!!! this method is not recomended becasue of fake views , we use ajax instead.

    if course.situation == True: #when ever a course is lunched it changes the situtaion of the course
        course.situation = False
    else:
        course.situation = True
    course.save() #every changes in objects in database should be saves
    return render(request , 'courses_app/courses_detail.html' , context={'course' : course})


def add_course(request):
    #attemped_title = request.GET.get('title') #this title and description names are from the name attributes of our form in add_course.html
    #attemped_description = request.GET.get('description') | #we don't use thig method , we use post method instead but now for educational perpose we did this
    #https://localhost:8080/courses/add?name=erfan&l=safarali : after ? sign we set key value pairs to send it
    #Course.objects.create(title = attemped_title , description = attemped_description) : here we create object , !!! title and description are fields of our model !!!!

    attemped_title = request.POST.get('title')
    attemped_description = request.POST.get('decsription')
    if attemped_title and attemped_description : #when you visit the page it sends the get request and field are empty so it returns error  so we only run this code if field are fiiled
        Course.objects.create(title=attemped_title, description=attemped_description , views=0)
        redirect('/courses/list')

    return render(request , 'courses_app/add_course.html')