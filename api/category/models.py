from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    
    #id=models.IntegerField(primary_key=False)
    #c_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    description=models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.id) + ' . ' + self.name