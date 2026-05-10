from django.db import models
from SchoolApp.models import SchoolProfileModel
from django.contrib.auth.models import User
# Create your models here.
GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)
class StudentProfileModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=GENDER)
    phoneNo=models.IntegerField()
    schoolName=models.ForeignKey(SchoolProfileModel, on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
    