from __future__ import unicode_literals
from django.db import models


class State(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()


class Priority(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Priorities'
