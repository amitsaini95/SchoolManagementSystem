from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from BaseApp.models import User
from StudentApp.models import *
from SchoolApp.models import *
from django.contrib.auth.hashers import make_password

from django.contrib.auth import get_user_model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    unique_profiles = StudentProfileModel.objects.filter(user=instance).distinct()
    unique_profiles.delete() 
    if  created:
        instance.set_password(instance.password)
        instance.save()
        if instance.userType=="admin":
            instance.is_staff=True
            instance.save()
        if instance.userType=="student":
            StudentProfileModel.objects.create(user=instance,name=instance.username)