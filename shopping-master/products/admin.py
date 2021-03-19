from django.contrib import admin
from .models import Product,ProductImage,Image,ListwaData

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model=Product
    list_display=['title','price','slug','update','active']
    search_fields=['title','description']
    list_filter=['title','price']
    list_editable=['price']
    prepopulated_fields={'slug':('title',)}

class ProductImageAdmin(admin.ModelAdmin):
    class Meta:
        model=ProductImage
    list_display=['product','featured','thumbnail','active']

class ImageAdmin(admin.ModelAdmin):
    class Meta:
        model=Image
    list_display=['photo','date_created']

class ListwaDataAdmin(admin.ModelAdmin):
    class Meta:
        model=ListwaData
    list_display=['photo_data']

admin.site.register(Product,ProductAdmin) 
admin.site.register(ProductImage,ProductImageAdmin) 
admin.site.register(Image,ImageAdmin)
admin.site.register(ListwaData,ListwaDataAdmin)