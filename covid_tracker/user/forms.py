from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name = forms.CharField(max_length=50, label='Doctor incharged', required=True)
    last_name=forms.ChoiceField(choices=((1,"Patient"),(2,"Doctor")),label="Select your choice")
    last_name.widget.attrs.update({'class':'form_choice'})
    #last_name= forms.CharField(max_length=50,label='Tell Something about yourself',required=False)

    class Meta:
        model=User 
        fields=['username','email','password1','password2','first_name','last_name']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50, label='Doctor incharged', required=True)
    last_name = forms.ChoiceField(choices=((1, "Patient"), (2, "Doctor")),label="Select your choice")
    last_name.widget.attrs.update({'class':'form_choice'})
    class Meta:
        model=User
        fields = ['username', 'email','first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['image','Age','tippler']