# -*- coding: utf-8 -*-
from django.conf.urls import url
from app import views
from app.views import *
import app.views as views


urlpatterns = [
    url(r'^$', Registro.as_view(), name='registro'),
    url(r'^registrado/$', Registrado.as_view(), name='registrado'),
    url(r'^consulta/$', Consulta.as_view(), name='consulta'),
]
