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
    user=serializers.StringRelatedField()
   
    class Meta:
        model=SchoolProfileModel
        
        fields=('id','name','code','SchoolPhoneNo','teachers','user','students','teachers','SchoolEmail','SchoolAddress','PrincipleName','PrinciplePhoneNo','PrincipleEmail','created','updated')
    def to_representation(self, instance):
        rep=super(SchoolSerializers,self).to_representation(instance)
        return rep
 
   
 
