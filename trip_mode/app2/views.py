from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def login(req):
    if req.method =='POST':
#        return (req,'login.html')
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(req,user)
            return redirect("/")
        else:
            messages.info(req,"invalid")
            return redirect('login')
    return render(req,'login.html')
def registration(val):
    if val.method == 'POST':
        username = val.POST['username']
        first_name = val.POST['firstname']
        last_name = val.POST['lastname']
        email = val.POST['email']
        password = val.POST['password']
        c_password= val.POST['password1']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(val, 'existing username')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(val, 'existing email id')
                return redirect('registration')
            elif User.objects.filter(password=password).exists():
                messages.info(val, 'existing password')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                                   password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(val, 'password not matching')
            return redirect('registration')
        return redirect('/')
    return render(val, "registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

