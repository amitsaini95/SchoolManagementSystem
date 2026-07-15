from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.
from rest_framework  import status
from SchoolApp.models import *
from rest_framework import mixins
from rest_framework import generics
class SchoolApiListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = SchoolProfileModel.objects.all()
    serializer_class = SchoolSerializers
    def perform_create(self,serializer):
        username=serializer.validated_data['name']
        print(username)
        user=User.objects.create(username=username,userType="school")
        user.set_password(username[:3]+"@123")
        user.save()
        serializer.save(admin=user)
      
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)