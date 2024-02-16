from django.urls import path
from . import views

urlpatterns = [
    path('info' , views.info),
    path('<username>' , views.profile),
]

# urls will be executed from up to down , it two urls have a same destination the upper url will work