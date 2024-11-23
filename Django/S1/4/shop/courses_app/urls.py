
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.courses_list),
    path('detail/<int:course_id>', views.course_detail),
    path('add' , views.add_course)
]
