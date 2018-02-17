# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Minuta(models.Model):
    responsable = models.CharField(max_length=50,blank=True,null=True)
    asistentes = models.TextField(max_length=2000,blank=True,null=True)
    asunto = models.CharField(max_length=200,blank=True,null=True)
    fecha = models.CharField(max_length=50,blank=True,null=True)
    hora_inicio = models.CharField(max_length=50,blank=True,null=True)
    hora_final = models.CharField(max_length=50,blank=True,null=True)
    puntos = models.TextField(max_length=2000,blank=True,null=True)
    acuerdos = models.TextField(max_length=2000,blank=True,null=True)

    def __unicode__(self):
        return self.responsable
