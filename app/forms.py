# -*- coding: utf-8 -*-
from django import forms
from .models import Minuta
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)


class MinutaForm(forms.ModelForm):

    responsable = forms.CharField(label="Responsable", widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Responsable',
            'data-placement':'right', 'data-container':'body',
        }), required = True)
    
    class Meta:
        model = Minuta
        fields = '__all__'
