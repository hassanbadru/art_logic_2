# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserAction(models.Model):
    operation = models.CharField(max_length=100, default='encoding')
    input = models.CharField(max_length=100, default='8191')
    result = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.operation + ' ' + self.input
