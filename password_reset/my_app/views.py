from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Createuser
# Create your views here.

@login_required(login_url='loginpage')
def home(request):
    return render(request,'home.html')



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=Createuser
        if request.method=='POST':
            form=Createuser(request.POST)
            if form.is_valid():
                form.save()
        context={
            "form":form
        }
        return render(request,'register.html',context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f"logged in as {request.user}")
                return redirect('home')
            else:
                messages.warning(request,'Wrong credentials')
                return redirect('loginpage')
        return render(request,'login.html')

def Logout(request):
    logout(request)
    messages.warning(request,'You have been logged out')
    return redirect('loginpage')