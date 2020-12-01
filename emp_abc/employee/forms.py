import django.forms
from django.forms import forms, ModelForm
from .models import Employee

class NewEmployeeForm(forms.Form):
    pass

class MNewEmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"