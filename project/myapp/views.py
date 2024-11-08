from pyexpat import model
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Details
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import model_to_dict

# SIGN UP FUNCTION

def signup(request):
    if request.method == "POST":
        name  = request.POST['name']
        email = request.POST['email'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.warning(request," password incorrect !")
            return redirect('signup')
        else:
            obj = User.objects.create_user(username=name,email=email,password=password1)
            obj.save()
            messages.success(request, "Registeration Successfully!")
            return redirect('signin')
    else:
        return render(request,"loginup.html")  

# SIGN IN FUNCTION

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "login successfully !")
                return redirect('home')
            else:
                messages.error(request,"login failed !")
                return render('signin')
    form = Details()
    return render(request,'login.html') 
 
# HOME PAGE

def home(request):
    return render(request,'create.html')

############################################################################################################
                      ####### CRUD OPERATION #####


# CREATE function for CRUD

def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        degree=request.POST['degree']
        address=request.POST['address']
        obj=Details.objects.create(name=name ,age=age,gender=gender,degree=degree,address=address)
        obj.save()
        
        return redirect('retrieve')

#  VIEW function for CRUD   
 
def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html',{'details':details})


# EDIT function for CRUD

def edit(request,id):
    object = Details.objects.get(id=id)
    return render(request,'popup.html',{'object': object})
    
    
def post(request,id):
    data = Details.objects.get(id=id)
    data_dict = model_to_dict(data)
    return JsonResponse(data_dict,safe=False)
    
 
#update function for CRUD   

def update(request,id):
    obj=Details.objects.get(id=id)
    if request.method=="POST":
        obj.name=request.POST['name']
        obj.age=request.POST['age']
        obj.gender=request.POST['gender']
        obj.degree=request.POST['degree']
        obj.address=request.POST['address']
        obj.save()
        return redirect('retrieve')   

# delete function for CRUD

def delete(request,id):
    object = Details.objects.get(id=id)
    object.delete()
    return redirect('retrieve')

def popup(request):
    return render(request,'popup.html')



