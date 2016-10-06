#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import *
from .forms import MinutaForm



class Registro(CreateView):
	template_name = "app/registro.html"
	model = Minuta
	form_class = MinutaForm
	#fields = ['responsable', 'asistentes', 'asunto', 'fecha', 'hora_inicio', 'hora_final', 'puntos', 'acuerdos']
	success_url = reverse_lazy('registrado')



class Registrado(TemplateView):
	template_name = "app/registrado.html"



class Consulta(ListView):
	model = Minuta
	fields = ['responsable', 'asistentes', 'asunto', 'fecha', 'hora_inicio', 'hora_final', 'puntos', 'acuerdos']
	template_name = "app/consulta.html"
	context_object_name = "lista"