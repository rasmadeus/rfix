from __future__ import unicode_literals
from django.db import models


class Page(models.Model):
    lang = models.CharField(max_length=2)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
