# -*- encoding: utf-8
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SEX_CHOICES = (
    ('M', 'Муж'),
    ('F', 'Жен'),
    )
 
    sex = models.CharField(choices=SEX_CHOICES, max_length=3)
# Create your models here.

"""
class CUser(models.Model):
    
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sex = models.CharField(choices=SEX_CHOICES, max_length=3)
 """ 
    
