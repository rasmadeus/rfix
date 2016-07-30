from __future__ import unicode_literals
from django.db import models
from rfix.rfixuser.models import RfixUser as User
from django.utils.translation import ugettext_lazy as tr


class Priority(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()

    class Meta:
        verbose_name = tr('Priority')
        verbose_name_plural = tr('Priorities')


class State(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()


class Kind(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()


class Comment(models.Model):
    reporter = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    reporter = models.ForeignKey(
        User,
        related_name='user_reporter',
        null=True,
        on_delete=models.SET_NULL
    )

    performer = models.ForeignKey(
        User,
        related_name='user_performer',
        null=True,
        on_delete=models.SET_NULL
    )

    tester = models.ForeignKey(
        User,
        related_name='user_tester',
        null=True,
        on_delete=models.SET_NULL
    )

    priority = models.ForeignKey(
        Priority,
        null=True,
        on_delete=models.SET_NULL
    )

    state = models.ForeignKey(
        State,
        null=True,
        on_delete=models.SET_NULL
    )

    kind = models.ForeignKey(
        Kind,
        null=True,
        on_delete=models.SET_NULL
    )

    comments = models.ManyToManyField(Comment)
