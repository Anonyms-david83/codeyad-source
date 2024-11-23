from django.urls import path
from . import views

urlpatterns = [
    path('info' , views.info),
    path('profile/<temped_username>' , views.profile),
    path('userlist' , views.userlist)
]

# urls will be executed from up to down , it two urls have a same destination the upper url will work