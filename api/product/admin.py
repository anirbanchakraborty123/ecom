from django.contrib import admin
from .models import  Product


# Register your models here.

# FOR UPLOADING MULTIPLE IMAGES
#class ImageAdmin(admin.StackedInline):
 #   model = Image
#class ImageAdmin(admin.ModelAdmin):
 #   pass
#admin.site.register(Image, ImageAdmin)
    
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at','id' )
    #inlines = [ImageAdmin]
    
admin.site.register(Product, ProductAdmin)

