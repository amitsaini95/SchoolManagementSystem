from django.db import models
from SchoolApp.models import *
from BaseApp.models import User
from TeacherApp.models import TeacherProfileModel
# Create your models here.

GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)
streamClass=(
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VIII', 'VIII'),
        ('IX', 'IX'),
        ('X', 'X'),
        ('XI', 'XI'),
        ('XII', 'XII'),
)

class StudentClass(models.Model):
    name = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"
class SessionModel(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return "From " + str(self.start_year) + " to " + str(self.end_year)
class CourseModel(models.Model):
    name = models.CharField(max_length=255)
    studentClass=models.CharField(choices=streamClass, max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"


class StudentProfileModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=10,choices=GENDER)
    stuclass=models.CharField(max_length=10,choices=streamClass)
    courses=models.ForeignKey(CourseModel,on_delete=models.CASCADE,related_name="stucourse",blank=True,null=True)
    phoneNo=models.IntegerField(null=True)
    schoolName=models.ForeignKey('SchoolApp.SchoolProfileModel', on_delete=models.CASCADE,related_name="schoolName",blank=True,null=True)
    email=models.EmailField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class SubjectModel(models.Model):
    name = models.CharField(max_length=255)
    course=models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

  

    

class AttendanceReport(models.Model):
    teacher=models.ForeignKey('TeacherApp.TeacherProfileModel', on_delete=models.CASCADE,null=True,blank=True)
    student = models.ForeignKey('StudentProfileModel', on_delete=models.DO_NOTHING)
    subject=models.ForeignKey('SubjectModel',on_delete=models.CASCADE)
    attendanceDate=models.DateField()
    status = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user} on {self.attendanceDate} date"
    