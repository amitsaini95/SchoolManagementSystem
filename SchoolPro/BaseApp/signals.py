from django.db.models.signals import post_save
from django.dispatch import receiver
from BaseApp.models import User
from StudentApp.models import *
from SchoolApp.models import *
def create_profile(sender, instance, created, **kwargs):
    if instance.userType=="student":
        StudentProfileModel.objects.create(user=instance,name=instance.username)
    elif instance.userType=="school":
        SchoolProfileModel.objects.create(admin=instance,name=instance.username)
post_save.connect(create_profile, sender=User)