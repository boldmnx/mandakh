from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'id': 'Код',
            'pname': 'Нэр',
            'price': 'Үнэ',
            'pdesc': 'Тайлбар',
            'cat': 'Ангилал'
        }
