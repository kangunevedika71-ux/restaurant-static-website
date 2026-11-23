from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def menu(request):
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')

def reservation(request):
    return render(request,'reservation.html')
    