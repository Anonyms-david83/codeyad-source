from django.contrib import admin
from .models import Course
# >>createsuperuser : we create an admin user


admin.site.register(Course)