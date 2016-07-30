from __future__ import unicode_literals
from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()


class Priority(Property):
    class Meta:
        verbose_name_plural = 'Priorities'


class State(Property):
    pass


class Type(Property):
    pass
