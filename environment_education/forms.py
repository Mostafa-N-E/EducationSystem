from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField, ChoiceField, formset_factory
from django import forms

from persons.models import Student
from .models import Class


# class CreateClassForm(forms.Form):
#
#     class Meta:
#         model = Class
#         fields = ('name', 'college','status',)


class CreateClassForm(forms.Form):
    name = forms.CharField(label='عنوان کلاس', max_length=50, required=False)
    college = forms.CharField(max_length=30, label='دانشکده', required=False)
    STATUS_CHOICE = [
        (1, 'Opened'),
        (0, 'Colsed'),
    ]
    status = forms.ChoiceField(label='وضعیت', required=False,choices=STATUS_CHOICE)


