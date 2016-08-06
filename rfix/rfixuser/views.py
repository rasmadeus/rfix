from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rfix.rfixuser import models


class RfixUserDetail(DetailView):
    model = models.RfixUser
    context_object_name = 'rfixuser'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RfixUserDetail, self).dispatch(*args, **kwargs)
