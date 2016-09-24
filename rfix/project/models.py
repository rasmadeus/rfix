from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from rfix.task.models import Task


class Project(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    tasks = models.ManyToManyField(Task, related_name='tasks', blank=True)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})
