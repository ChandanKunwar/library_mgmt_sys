from django import forms
from django.forms import ModelForm
from django.forms.fields import Field
from .models import *

class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()

class BookModelForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'