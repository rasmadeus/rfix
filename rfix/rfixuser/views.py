from django.views.generic.detail import DetailView
from django.utils.translation import ugettext_lazy as tr
from rfix.rfixuser import models
from rfix.page.models import Page


class RfixUserDetail(DetailView):
    model = models.RfixUser
    context_object_name = 'rfixuser'

    def get_context_data(self, **kwargs):
        context = super(RfixUserDetail, self).get_context_data(**kwargs)
        context['page'] = Page.guest_default()
        context['email'] = 'rasmadeus@gmail.com'
        context['links'] = (
            {'name': tr('Support'), 'href': '/support'},
            {'name': tr('Login'), 'href': '/users/login'}
        )
        return context

