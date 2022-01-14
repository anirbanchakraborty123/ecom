from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomeUser(AbstractUser):
    
    name=models.CharField(max_length=50,default='Anonymous')
    email=models.EmailField(max_length=100 , unique=True)
    
    username= None
    
    USERNAME_FIELD= 'email'
    
    #IF YOU WANT ANY FIELD TO BE REQUIRED OR MANDATORY WHILE FILLING FORM 
      # WE CAN ADD THOSE FIELD INSIDE THAT LIST
    REQUIRED_FIELDS=[]
    
    session_token=models.CharField(max_length=10, default=0)
    
    created_at=models.DateTimeField(auto_now_add=True)  
    updated_at=models.DateTimeField(auto_now=True)          