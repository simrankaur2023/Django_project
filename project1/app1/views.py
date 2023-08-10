from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your views here.

def Index(request):
    return HttpResponse("select the day of week")
def menu(request):
    return render (request,'index.html')
def contact(request):
    return render (request,'contact.html')
def about(request):
    return render (request,'about.html')
def home(request):
    return render (request,'home.html')
def work(request,days):
    return render(request , 'work.html',{"Day":days})