from fileinput import FileInput

from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Textarea

from mainapp.models import Goods


class AddProductForm(ModelForm):
    class Meta:
        model = Goods
        fields = ['name', 'description', 'price', 'quantity', 'img_product']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название продукта'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание продукта'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'цена'
            }),
            'quantity': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'количество'
            })
        }



