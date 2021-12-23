from .models import Health
from django import forms
from django.contrib.auth.models import User

class ReportCreationForm(forms.ModelForm):
    patient=forms.ModelChoiceField(queryset=User.objects.all())
    o2_level=forms.IntegerField()
    bp_level=forms.IntegerField()
    sugar_level=forms.IntegerField()
    crp=forms.DecimalField(decimal_places=2,max_digits=2)
    Feedback=forms.CharField(max_length=100,label="Feedback",required=True)
    patient.widget.attrs.update({'class':'form_choice'})
    class Meta:
        model=Health
        fields=['patient','o2_level','bp_level','sugar_level','crp','Feedback']
        
