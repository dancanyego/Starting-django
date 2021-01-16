from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    return render(request,'DEMOAPP/hi.html')

# Create your views here.
