from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    #to show id field in rest_framework json response 
    id = serializers.ReadOnlyField()

    image = serializers.ImageField(max_length=None,
            allow_empty_file=False,allow_null=True,required=False)
    
    
    #to show the category name instead of category url in json response
    category= serializers.ReadOnlyField(source='category.name')    


    class Meta:
        
        model= Product
        
        #fields = ['id','name','description']
        fields= '__all__'