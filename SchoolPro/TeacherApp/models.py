from django.db import models
from BaseApp.models import User
from SchoolApp.models import *
# Create your models here.
class TeacherProfileModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(null=True)
    email=models.EmailField(max_length=254)
    preSchoolName=models.CharField(max_length=50)
    newSchoolName=models.ForeignKey("SchoolApp.SchoolProfileModel", on_delete=models.CASCADE,related_name="teacherSchool")
    address=models.TextField()
    qualification=models.CharField(max_length=50)
    experience=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

  