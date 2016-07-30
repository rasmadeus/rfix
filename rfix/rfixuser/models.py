from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.urlresolvers import reverse


class RfixUser(AbstractUser):
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='rfixusers')

    def get_absolute_url(self):
        return reverse('detail', args=self.slug)
