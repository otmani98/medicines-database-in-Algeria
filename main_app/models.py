from django.db import models

class MedicinesModel(models.Model):

    registration_no = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    inn = models.CharField(max_length=150)
    bn = models.CharField(max_length=150)
    form = models.CharField(max_length=150)
    dosing = models.CharField(max_length=150, null=True)
    cond = models.CharField(max_length=150, null=True)
    list = models.CharField(max_length=150, blank=True,null=True)
    p1 = models.CharField(max_length=150, blank=True,null=True)
    p2 = models.CharField(max_length=150, blank=True,null=True)
    obs = models.CharField(max_length=150, blank=True,null=True)
    laboratories = models.CharField(max_length=150)
    country = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.bn