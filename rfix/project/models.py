from __future__ import unicode_literals
from django.db import models
from rfix.task.models import Task


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    tasks = models.ManyToManyField(Task)
