from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.
import json
from rest_framework  import status
from SchoolApp.models import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import *
class SchoolApiListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = SchoolProfileModel.objects.all()
    serializer_class = SchoolSerializers
    authentication_classes=[BasicAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]
 
      
    def perform_create(self, serializer):
        name=serializer.validated_data['name']
        user=User.objects.create(username=name,userType="school")
        user.set_password(name[:3]+"@123")
        user.save()
        # Automatically saves the current logged-in user as the owner
        serializer.save(user=user)
       
        
 
    def get(self, request, *args, **kwargs):
        

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      

        # Continue with the standard Django view execution chain
    
        
        return self.create(request, *args, **kwargs)
class SchoolAPIDetails(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    queryset = SchoolProfileModel.objects.all()
    serializer_class = SchoolSerializers

    def perform_update(self,instance,*args, **kwargs):
        username=instance['user'].value
        name=instance.validated_data['name']
        user=User.objects.get(username=username)
        user.username=name
        user.set_password(name[:3]+"@123")
        user.save()
        id=instance.data['id']
        school=SchoolProfileModel.objects.get(id=id)
        serializer = SchoolSerializers(school, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        school=SchoolProfileModel.objects.get(id=id)
        user=User.objects.get(username=school.user)
        user.delete()
        return self.destroy(request, *args, **kwargs)