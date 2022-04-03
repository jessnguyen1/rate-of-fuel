from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.files import File


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)

        if user is not None:
            login(request,user)
            return render(request,"authentication/client.html")
        else:
            messages.error(request,"Incorrect Username or Password")
            return redirect('signin')



    return render(request,"authentication/login.html")

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = "sample@sample.com"

        myUser = User.objects.create_user(username,email,password)
        myUser.save()

        messages.success(request,"Successful")

        return redirect('signin')



    return render(request,"authentication/Register.html")


def client(request):
    if request.method == "POST":
        fullName = request.POST['fullname']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']

        f = open("myfile.txt", "w")
        f.write(fullName)
        f.write(address1)
        f.write(address2)
        f.write(city)
        f.write(state)
        f.write(zipcode)
        f.close()

    return render(request,"authentication/client.html")

def profilemanagement(request):
    f = open("myfile.txt", "w")
    
    if request.method == "POST":
        fullName = request.POST['name']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        
        f.seek(0)
        f.write(fullName)
        f.write(address1)
        f.write(address2)
        f.write(city)
        f.write(state)
        f.write(zipcode)
        f.truncate()
        f.close()
        
    return render(request, 'authentication/Client Profile Management.html')