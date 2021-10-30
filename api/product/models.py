from django.db import models
from api.category.models import Category

# Create your models here.
class Product(models.Model):
    
    #p_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    price= models.FloatField()
    discount_price= models.FloatField(default=True,null=True,blank=True)
    stock= models.FloatField()
    is_active=models.BooleanField(default=True,blank=True)
    image=models.ImageField(blank=True,null=True,upload_to='images/')
    description=models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now_add=True,)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,default=True,blank=True,null=True)
    
    
    def __str__(self):
        return str(self.id) + ' . ' + self.name
   
   # FOR IMPLEMENTING MULTIPLE IMAGES UPLOAD 
# class Image(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE) 
#     image= models.ImageField(upload_to='images/',null=True,blank=True)

#     def __str__(self):
#         return str(self.product) 
    
    
