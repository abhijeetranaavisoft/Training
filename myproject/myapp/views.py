from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
#from .models import Feature





# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check if the username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use')
                return redirect('register')
            else:
                # Create the new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
   if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']

      user=auth.authenticate(username=username,password=password)

      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         messages.info(request,'Credentials invalid')
         return redirect('login')
   else:
    return render(request,'register.html')
        

def index(request):
   return render('request','index.html')

def logout(request):
   auth.logout(request)
   return redirect('/')

def counter(request):
   posts=[1,2,3,4,5,'tim','tom','john']
   return render(request,'counter.html',{'posts':posts})

def post(request,pk):
   return render(request,'post.html',{'pk':pk})
"""
def index(request):
    #feature1=Feature()
    #feature1.id=0
    #feature1.name='Fast'
    #feature1.details='Our service is very quick'
    #similarly we have four different types of feature
    #features=[feature1,feature2,feature3,]
    #features=Feature.object.all()// this data is coming from databasase
    context={
        'name':'patrrick',                                                                
        #'name':user.name this  data coming from database
        'age':23,
        'nationality':'British',
    }
    return render(request,'index.html',context)
    #return render(request,'index.html',context,{'feature1':feature1})
 # text=request.GET['text']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
def counter(request):
    text=request.POST['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})
    """