from django import forms


class SignupForm(forms.Form):
    fname = forms.CharField(label='Нэр')
    lname = forms.CharField(label='Овог')
    email = forms.EmailField(label='Мэйл')
    password = forms.CharField(widget=forms.PasswordInput(), label='нууц үг')
    repassword = forms.CharField(
        widget=forms.PasswordInput(), label='нууц үг давтах')
