# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Minuta(models.Model):
    responsable = models.CharField(max_length=50)
    asistentes = models.TextField(max_length=2000)
    asunto = models.CharField(max_length=200)
    fecha = models.CharField(max_length=50)
    hora_inicio = models.CharField(max_length=50)
    hora_final = models.CharField(max_length=50)
    puntos = models.TextField(max_length=2000)
    acuerdos = models.TextField(max_length=2000)

    def __unicode__(self):
        return self.responsable
