from django.db import models
from BaseApp.models import User
from StudentApp.models import StudentProfileModel
# Create your models here.
class SchoolProfileModel(models.Model):
    admin=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=150)
    code=models.IntegerField(null=True)
    SchoolEmail=models.EmailField(max_length=100)
    SchoolPhoneNo=models.IntegerField(null=True)

    SchoolAddress=models.TextField()
    SchoolEmail=models.EmailField(max_length=100)
    PrincipleName=models.CharField(max_length=100)
    PrinciplePhoneNo=models.IntegerField(null=True)
    PrincipleEmail=models.EmailField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.name

