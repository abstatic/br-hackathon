# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Employee(models.Model):
    e_id = models.CharField(primary_key=True, max_length=10)
    e_name = models.CharField(max_length=30)
    e_type = models.CharField(max_length=15)
    def __str__(self):
        return self.e_name

class TimeRecord(models.Model):
    RECORD_TYPES = (('IN', 'In'), ('OUT', 'Out'))
    time_names = models.CharField(max_length=5, choices=RECORD_TYPES)
    time_record = models.DateTimeField()
    e_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

admin.site.register(Employee)
admin.site.register(TimeRecord)
