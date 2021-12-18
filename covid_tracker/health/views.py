from django.shortcuts import render,get_object_or_404
from .models import Health
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

class ReportCreateView(LoginRequiredMixin,CreateView):
    model=Health

    fields = ['patient','o2_level','bp_level','sugar_level','crp','Feedback']

    def form_valid(self, form):
        return super().form_valid(form)


def get_report(request):
    avail=0
    if request.method=="POST":

        username=request.POST["username"]
        objs=Health.objects.all()
        o2=[]
        bp=[]
        sugar=[]
        crp=[]
        x=[]
        count=0
        time=[]
        for person in objs:
            if person.patient.username==username:
                avail=1
                o2.append(person.o2_level)
                bp.append(person.bp_level)
                sugar.append(person.sugar_level)
                crp.append(float(person.crp))
                count+=1
                time.append(str(person.report_date))
                x.append(count)

        context={"user":username,"o2":o2,"bp":bp,"sugar":sugar,"crp":crp,"data":o2,"labels":time,"avail":avail,"msg":"Enter valid username"}
        return render(request,"health/chart.html",context=context)
    else:
        return render(request, "health/chart.html",context={"avail":avail,"msg":"Enter valid username"})