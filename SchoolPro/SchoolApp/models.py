from django.db import models
from BaseApp.models import User
from StudentApp.models import StudentProfileModel
from TeacherApp.models import TeacherProfileModel
# Create your models here.
class SchoolProfileModel(models.Model):
    admin=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,related_name="schoolUser")
    name=models.CharField(max_length=150)
    code=models.IntegerField(null=True)
    SchoolPhoneNo=models.IntegerField(null=True)
    students=models.ManyToManyField(StudentProfileModel,blank=True)
    teachers=models.ManyToManyField(TeacherProfileModel,blank=True)
    SchoolAddress=models.TextField()
    SchoolEmail=models.EmailField(max_length=100)
    PrincipleName=models.CharField(max_length=100)
    PrinciplePhoneNo=models.IntegerField(null=True)
    PrincipleEmail=models.EmailField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.name

class EmailSchoolNotificationModel(models.Model):
    user=models.ForeignKey(SchoolProfileModel, on_delete=models.CASCADE)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
    