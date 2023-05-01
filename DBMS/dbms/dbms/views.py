from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render

def home(req):
    return render(req,'home.html',{})


def user_login(req):
    if req.method=='POST':
        err_msg=None

        username=req.POST['username']
        password=req.POST['password']
        user= authenticate(req,username=username, password=password)

        if user is not None:
            login(req,user)
            err_msg="Login Successfull!!"
            return render(req,'home.html',{'err_msg':err_msg})
        else:
            err_msg="Please enter a valid username and password!"
        
        context={
            "err_msg":err_msg,
        }

        print(err_msg)

        return render(req,'login.html',context)
    return render(req,'login.html')


def logout_view(request):
    logout(request)
    return render(request,'home.html')