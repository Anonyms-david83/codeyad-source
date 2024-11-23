from django.db import models

class Course(models.Model):  #all models should inherits from models.Model
    title = models.CharField(max_length=30) #charfield is character field , max_lenghth declears maximum lenght of the table
    description = models.TextField(max_length=50) #textfield always accept only texts nothing more
    situation = models.BooleanField(default=False) #boleanfield is for being true of false , default = the default value of the property
    views = models.IntegerField(default=0 , null=True)
    image = models.ImageField(null=True , upload_to="codeyad")#uplaod_to is the place that the imgs will be saved

# >>makemigrations : it temperorary create changed in database with 001_initial files in migrations folder

# >>migrate : it applies the changes in database

    def __str__(self):       #when object is called , the name of the object will be self.title now like in admin panel's objects list
        return f"{self.title} - {self.description[:30]}"
