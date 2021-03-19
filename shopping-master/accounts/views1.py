from django.shortcuts import render,redirect

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib import auth





# Create your views here.



def login(request):

        if request.method == "POST":

                username=request.POST['username']

                password=request.POST['password']



                user=auth.authenticate(username=username,password=password)



                if user is not None:

                        auth.login(request,user)

                        messages.success(request,"succesfully logged in")

                        return redirect('product')

                else:

                        messages.error(request,"Invalid credentials")

                        return redirect('login')



        return render(request,'accounts/login.html')



def register(request):

    if request.method == 'POST':

        first_name=request.POST['first_name']

        last_name=request.POST['last_name']

        username=request.POST['username']

        email=request.POST['email']

        password=request.POST['password']

        password2=request.POST['password2']

        if password == password2:

                if User.objects.filter(username=username).exists():

                        messages.error(request,"Username already exists")

                        return redirect('register')

                elif User.objects.filter(email=email).exists():

                        messages.error(request,"Email already exists")

                        return redirect('register')

                else:

                        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)

                        user.save()

                        messages.success(request,"You have been successfully registered")

                        return redirect('login')

        else:

                messages.error(request,"Password did not match")

                return redirect('register')

    else:

            return render(request,'accounts/register.html')



def logout(request):

        if request.method=="POST":

                auth.logout(request)

                messages.success(request,"You have been logged out")

                return redirect('product')

        return redirect('product')

