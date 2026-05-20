from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
user_type=(
    ('admin','admin'),
    ('student','student'),
    ('school','school'),
    ('teacher','teacher')
)
from django.db.models.signals import post_save

from django.utils import timezone

class User(AbstractUser):
    userType=models.CharField(choices=user_type, max_length=50,default="admin")
    def __str__(self):
        return self.username
