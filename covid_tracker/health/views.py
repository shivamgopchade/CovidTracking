from django.shortcuts import render,get_object_or_404,redirect
from .models import Health
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import ReportCreationForm
# Create your views here.

def create_report(request):
    if request.method=='POST':
    
        uform=ReportCreationForm(request.POST)
        if uform.is_valid():
            uform.save()
            return redirect('home')

    
    else:
    
        ufrom=ReportCreationForm()
        return render(request,'health/health_form.html',context={'form':ufrom})
    

# class ReportCreateView(LoginRequiredMixin,CreateView):
#     model=Health

#     fields = ['patient','o2_level','bp_level','sugar_level','crp','Feedback']

#     def form_valid(self, form):
#         return super().form_valid(form)


def get_report(request):
        if request.method=="POST":
            username=request.POST["username"]
            
        else:
            username=request.user.username
        
        objs=Health.objects.all()
        o2=[]
        bp=[]
        sugar=[]
        crp=[]
        time=[]
        avail=0
        for person in objs:
            if person.patient.username==username:
                avail=1
                o2.append(person.o2_level)
                bp.append(person.bp_level)
                sugar.append(person.sugar_level)
                crp.append(float(person.crp))
                time.append(str(person.report_date))


        context={"username":username,"o2":o2,"bp":bp,"sugar":sugar,"crp":crp,"data":o2,"labels":time,"avail":avail}
        return render(request,"health/chart.html",context=context)