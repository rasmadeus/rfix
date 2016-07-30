from django.views.generic.detail import DetailView
from rfix.rfixuser import models


class RfixUserDetail(DetailView):
    model = models.RfixUser
    context_object_name = 'rfixuser'
