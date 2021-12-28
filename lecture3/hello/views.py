from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def tung(a):
    return HttpResponse("Hello Tung!!!")
def hanh(a):
    return HttpResponse("Hello Hanh!")
def greet(request,ame):
    return render(request, "hello/greet.html",{
        "name": ame.capitalize()
    })