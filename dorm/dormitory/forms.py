from .models import *
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    first_name = forms.CharField(max_length=32, required=True)
    last_name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    course = forms.CharField(max_length=32, required=True)
    contact_no = forms.CharField(max_length=32, required=True)
    birth_date = forms.DateField()
    mother_name = forms.CharField(label = 'Mother name', max_length = 120)
    mother_contact = forms.RegexField(label = "Mother contact Number", help_text = "Accepted Formats: '+999999999'. Up to 15 digits allowed.", regex = r'^\+?1?\d{9,15}$' )
    father_name = forms.CharField(label = 'Father name', max_length = 120)
    father_contact = forms.RegexField(label = "Father contact Number", help_text = "Accepted Formats: '+999999999'. Up to 15 digits allowed.", regex = r'^\+?1?\d{9,15}$' )
    guardian_name = forms.CharField(label = 'Guardian name', max_length = 120)
    guardian_contact = forms.RegexField(label = "Guardian contact Number", help_text = "Accepted Formats: '+999999999'. Up to 15 digits allowed.", regex = r'^\+?1?\d{9,15}$' )
    bunk = forms.ModelChoiceField(queryset=Bunk.objects.all())

class DManagerForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    first_name = forms.CharField(max_length=32, required=True)
    last_name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
