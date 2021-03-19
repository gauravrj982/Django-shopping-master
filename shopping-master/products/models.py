from django.db import models


# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=30,default=29)
    sales_price=models.DecimalField(decimal_places=2,max_digits=30,null=True,blank=True)
    slug=models.SlugField()
    timeStamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    update=models.DateTimeField(auto_now_add=False,auto_now=True)
    reverse_shipping=models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product/images',null=True)
    featured=models.BooleanField(default=False)
    thumbnail=models.BooleanField(default=False)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.product.title

class Image(models.Model):
    photo=models.FileField()
    date_created=models.DateTimeField(blank=True)

class ListwaData(models.Model):
    photo_data=models.TextField(max_length=10000)

  







