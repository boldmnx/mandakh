from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class UserProfileForm(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('user_img', 'user_site')
