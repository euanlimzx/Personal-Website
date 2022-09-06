from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"website/index.html")

def mystories(request):
    ##i wanna change this to accept arguments
    return render(request,"website/stories.html")

def professional(request):
    return render(request,'website/professional.html')

def about(request):
    return render(request,"website/about.html")