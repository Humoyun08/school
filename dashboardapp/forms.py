from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import *

class CreateMentorForms(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['full_name','fani','malumoti','sinfi',]
        
        
