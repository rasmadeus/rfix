from django.views.generic.detail import DetailView
from rfix.project import models


class ProjectDetail(DetailView):
    model = models.Project
    context_object_name = 'project'
