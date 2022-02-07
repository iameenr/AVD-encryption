from django.shortcuts import render, redirect
from .models import Administrators as Admin
from django.contrib import messages
# Create your views here.


def login(request):
    if(request.method == "POST"):
        name = request._post["username"]
        password = request._post["password"]
        admin = Admin.objects.filter(name=name, password=password)

        if(len(admin) <= 0):
            messages.error(
                request, message="Invalid Username or Password", extra_tags="danger")
            return redirect('/auth/login')
        elif(len(admin) == 1):
            admin = admin.first()
            request.session['admin'] = admin.name
            return redirect('/')

    try:
        if(request.session['admin']):
            return redirect('/')
    except KeyError:
        pass
    return render(request, 'userauth/login.html')


def logout(request):
    try:
        if(type(request.session['admin']) == str):
            del request.session['admin']
    except KeyError:
        print("Error in Logging Out!")
        return redirect('/auth/login')

    return redirect('/')


def error(request, exception):
    return render(request, 'userauth/error.html')
