from rest_framework import serializers
from SchoolApp.models import *
from StudentApp.models import *
from BaseApp.models import User
class SchoolUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')
    def create(self, validated_data):
        # Uses Django's create_user method to hash the password securely
        return User.objects.create_user(**validated_data)
    def to_representation(self, instance):
        rep=super(SchoolUserSerializers,self).to_representation(instance)
        return rep
class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model=SchoolProfileModel
        fields=('id','name','code','SchoolPhoneNo','admin','students','teachers','SchoolEmail','SchoolAddress','PrincipleName','PrinciplePhoneNo','PrincipleEmail','created','updated')
   
        
    def to_representation(self, instance):
        rep=super(SchoolSerializers,self).to_representation(instance)
        users=SchoolUserSerializers(User.objects.get(id=instance.admin.id))
      
        teacherList=[]
        studentList=[]
        for teacher in instance.teachers.all():
            teacherList.append({'id':teacher.id,'name':teacher.name,'age':teacher.age,'email':teacher.email,'preSchoolName':teacher.preSchoolName,'newSchoolName':instance.name,'address':teacher.address,'qualification':teacher.qualification,'experience':teacher.experience,'created':teacher.created,'updated':teacher.updated})
        for student in instance.students.all():
            studentList.append({'id':student.id,'name':student.name,'age':student.age,'gender':student.gender,'stuclass':student.stuclass,'emaill':student.email,'phoneNo':student.phoneNo,'created':student.created,'updated':student.updated})
        
  
        rep['admin']=users.data
        rep['students']=studentList
        rep['teachers']=teacherList
        return rep