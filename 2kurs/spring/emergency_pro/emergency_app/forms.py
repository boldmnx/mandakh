
from django import forms
from .models import User

class JoinQueueForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']
        labels={
            'name':'Нэр'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
        }
