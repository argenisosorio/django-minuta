# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Minuta(models.Model):
    responsable = models.CharField(max_length=50)

    def __unicode__(self):
        return self.responsable
