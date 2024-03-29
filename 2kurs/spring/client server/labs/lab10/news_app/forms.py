from django import forms
from .models import *
from datetime import datetime


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        labels = {
            'nname': 'Нэр',
            'npara': 'Мэдээ',
            'nchoose': 'Хүйс',
            'nognoo':  'Нийтэлсэн огноо',
            'cat': 'Ангилал',
        }
        widgets = {
            'npara': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            # 'nognoo':  forms.DateInput(attrs={'type': 'date'}),
            'nognoo':  forms.HiddenInput(),
        }
