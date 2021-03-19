from django.shortcuts import render,get_object_or_404
from .models import Product,ProductImage,Image,ListwaData
import pymysql
import base64
import urllib.parse
import time
import string
import random
from datetime import datetime

# Create your views here.

def home(request):
    template='products/home.html'
    return render(request,template)


def product(request):
    products=Product.objects.all()
    context={'products':products}
    template='products/product.html'
    return render(request,template,context)

def uniqueproduct(request,id):
    uniqueproducts=get_object_or_404(Product,pk=id)
    context={'uniqueproducts':uniqueproducts}
    template='products/uniqueproduct.html'
    return render(request,template,context)



def images(request):


    def random_name(size=6, chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for x in range(size))

    
    from firebase import firebase
    firebase=firebase.FirebaseApplication("https://esp32camtest.firebaseio.com/",None)
    result=firebase.get('/esp32-cam/','')
    data=[]
    for value1 in result.values():
        for value2 in value1.values():
            data.append(value2)

    listi=[]
    listwa=ListwaData.objects.all()
    for bhakam in listwa:
        listi.append(bhakam.photo_data)
    


    for new_data in data:
        if new_data in listi:
            pass
        else:
            now=datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            con = pymysql.connect(host = 'localhost',user = 'root',passwd = 'root',db = 'bhalla') 
            cursor = con.cursor()
            cursor.execute("INSERT INTO products_listwadata (photo_data) VALUES (%s)", (new_data))
            con.commit()
            con.close()

            path="C:/Users/rohit/WorkspacePython/static/media/"+ random_name()+".jpg"
            filter_data=urllib.parse.unquote(new_data.strip("data:image/jpeg;base64,"))
            fileData = base64.urlsafe_b64decode(filter_data.encode('UTF-8'))
            with open(path, 'wb') as theFile:
                theFile.write(fileData)

            con1 = pymysql.connect(host = 'localhost',user = 'root',passwd = 'root',db = 'bhalla') 
            cursor = con1.cursor()
            time.sleep(2)
            cursor.execute('INSERT INTO products_image (photo, date_created) values(%s, %s)', (path, formatted_date))
            con1.commit()
            con1.close()

    image_data=Image.objects.all()
    return render(request,'products/esp.html',{'image_data':image_data})


