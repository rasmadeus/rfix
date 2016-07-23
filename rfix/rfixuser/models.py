from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe


class RfixUser(AbstractUser):
    photo = models.ImageField(upload_to='rfixusers')
