import django.http
from django.shortcuts import render,redirect
from django.http import request
from django.http import HttpResponse

def home(request):
    user=request.user
    return render(request,"index.html",context={'user':user})