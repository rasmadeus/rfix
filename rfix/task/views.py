from django.views.generic.detail import DetailView
from rfix.task import models


class TaskDetail(DetailView):
    model = models.Task
    context_object_name = 'task'
