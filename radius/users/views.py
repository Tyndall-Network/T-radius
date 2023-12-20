# from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home_view(request, *args, **kwargs):
    """Home Page."""
    # login
    if request.method == 'POST':
        username = request.POST["username"]
        passwd = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=passwd)
        if user:
            login(request, user)
            messages.success(request, "Success!!")
            return redirect('home')
        else:
            messages.error(request, "Error Logging in!!")
            return redirect('home')
    else:
        # return HttpResponse("Hello World")
        return render(request, "home.html", {})


# def login_user(request, *args, **kwargs):
#    """LogIn."""
#    pass Do login in the home fxn


def logout_user(request, *args, **kwargs):
    """Logout."""
    logout(request)
    messages.success(request, "Bye!!")
    return redirect('home')
