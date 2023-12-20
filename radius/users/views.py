# from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    """Home Page."""
    # return HttpResponse("Hello World")
    return render(request, "home.html", {})
