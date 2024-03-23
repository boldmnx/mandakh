from django import forms
from django.forms import ModelChoiceField
from .models import *


class BranchForm(forms.Form):
    bname = forms.TextInput(),
    baddress = forms.Textarea(),
    bphone = forms.CharField()


class WorkerForm(forms.Form):
    wfname = forms.CharField()
    wlname = forms.CharField()
    wgender = forms.RadioSelect(choices=[
        ('Эр', 'Male'),
        ('Эм', 'Female')]),
    wphone = forms.CharField(),

    branch = ModelChoiceField(Branch.objects.all(), label='Салбар')

    labels = {
        'wlast': 'Овог',
        'branch': 'Салбар'
    }

    # branch = ModelChoiceField(queryset=[
    #     ('1', 'salbar-1'),
    #     ('2', 'salbar-2')
    # ])
