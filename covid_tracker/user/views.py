from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def UserRegistration(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,"user/register.html",context={"form":UserRegisterForm()})

@login_required
def profile(request):
    if request.method=="POST":
        uform=UserUpdateForm(request.POST,instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            return redirect('home')
    return render(request,'user/profile.html',context={"uform":UserUpdateForm(instance=request.user),"pform":ProfileUpdateForm(instance=request.user.profile)})

