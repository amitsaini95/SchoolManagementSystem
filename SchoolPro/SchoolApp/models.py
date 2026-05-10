from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SchoolProfileModel(models.Model):
    admin=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    code=models.IntegerField()
    SchoolEmail=models.EmailField(max_length=100)
    SchoolPhoneNo=models.IntegerField()
    SchoolAddress=models.TextField()
    SchoolEmail=models.EmailField(max_length=100)
    PrincipleName=models.CharField(max_length=100)
    PrinciplePhoneNo=models.IntegerField()
    PrincipleEmail=models.EmailField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.name

