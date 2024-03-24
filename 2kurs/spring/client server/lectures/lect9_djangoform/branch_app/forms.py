from django import forms


class BranchForm(forms.Form):
    bname = forms.CharField(label='Салбарын нэр')
