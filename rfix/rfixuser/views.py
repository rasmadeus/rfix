from django.views.generic.detail import DetailView
from django.utils.translation import ugettext_lazy as tr
from rfix.rfixuser import models
from rfix.task.models import Task


class RfixUserDetail(DetailView):
    model = models.RfixUser
    context_object_name = 'rfixuser'

    def get_context_data(self, **kwargs):
        context = super(RfixUserDetail, self).get_context_data(**kwargs)

        context['links'] = (
            {'name': tr('Support'), 'href': '/support'},
            {'name': tr('Login'), 'href': '/users/login'}
        )

        user = context['rfixuser']
        context['groups'] = (
            {
                'header': tr('Tasks to perform'),
                'tasks': Task.objects.filter(performer=user)
            },
            {
                'header': tr('Tasks to review'),
                'tasks': Task.objects.filter(reviewer=user)
            },
            {
                'header': tr('Tasks to test'),
                'tasks': Task.objects.filter(tester=user)
            },
        )

        return context
