from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def uploadFile(req):
    if req=='POST':
        if req.user.is_authenticated:
            file=req.GET['file']
            user=req.user
            f=File(file=file,user=user)
            f.save()

        return render(req,'Home.html',{'err_msg':"File Uploaded successfully!!"})
    return render(req,'Home.html',{'err_msg':None})
    
