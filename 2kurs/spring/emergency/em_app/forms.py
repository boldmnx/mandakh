from django import forms
from .models import *


class CostumerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
