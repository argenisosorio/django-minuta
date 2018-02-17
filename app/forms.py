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

    asistentes = forms.CharField(label="Asistentes", widget=Textarea(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Asistentes',
            'data-placement':'right', 'data-container':'body',
        }),required = False)

    asunto = forms.CharField(label="Asunto", widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Asunto',
            'data-placement':'right', 'data-container':'body',
        }), required = True)

    fecha = forms.CharField(label="Fecha", widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Fecha',
            'data-placement':'right', 'data-container':'body',
        }), required = True)
    
    hora_inicio = forms.CharField(label="Hora de inicio", widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Hora de inicio',
            'data-placement':'right', 'data-container':'body',
        }), required = True)

    hora_final = forms.CharField(label="Hora de finalizacion", widget=TextInput(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Hora de finalizacion',
            'data-placement':'right', 'data-container':'body',
        }), required = True)

    puntos = forms.CharField(label="Puntos tratados", widget=Textarea(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Puntos tratados',
            'data-placement':'right', 'data-container':'body',
        }),required = False)

    acuerdos = forms.CharField(label="Acuerdos", widget=Textarea(attrs={
            'class': 'form-control input-md','style': 'width: 100%;',
            'data-toggle': 'tooltip','title': 'Acuerdos',
            'data-placement':'right', 'data-container':'body',
        }),required = False)
    
    class Meta:
        model = Minuta
        fields = '__all__'
