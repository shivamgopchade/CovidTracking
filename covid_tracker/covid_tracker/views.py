import django.http
from django.shortcuts import render,redirect
from django.http import request
from django.http import HttpResponse
from health.models import Health
import datetime
from django.contrib.auth.models import User

def home(request):
    user=request.user
    if user.is_authenticated:
        l1=list(Health.objects.filter(patient=user))
        if len(l1)!=0:
            obj1=l1[-1]
            obj2=l1[0]
            date=obj2.report_date
            date_today=datetime.date.today()
            delta=(date_today-date).days
        else:
            delta=0
            date=0
    else:
        delta=0
        date=0
    return render(request,"index.html",context={'user':user,'date':date,"delta":delta})

def delete_user(request):
    try:
        obj=User.objects.get(username=request.user.username)
        obj.delete()
    except:
        pass
    return redirect('home')