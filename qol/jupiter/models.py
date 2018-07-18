# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    e_id = models.CharField(primary_key=True)
    e_name = models.CharField(max_length=30)
    e_type = models.CharField(max_lenth=15)
    def __str__(self):
        return self.e_name

class TimeRecord(models.Model):
    RECORD_TYPES = (('IN', 'In'), ('OUT', 'Out'))
    time_names = models.CharField(max_lenth=5, choices=RECORD_TYPES)
    time_record = models.DateTimeField()
    e_id = Models.ForeignKey(Employee, on_delete=Models.CASCADE)
