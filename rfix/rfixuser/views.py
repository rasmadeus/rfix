from django.views.generic.detail import DetailView
from django.utils.translation import ugettext_lazy as tr
from rfix.rfixuser import models
from rfix.task.models import Task
from rfix.rfixuser import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth


class RfixUserDetail(DetailView):
    model = models.RfixUser
    context_object_name = 'rfixuser'

    def get_context_data(self, **kwargs):
        context = super(RfixUserDetail, self).get_context_data(**kwargs)

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


def login(req):
    if req.method == 'POST':
        form = forms.Login(req.POST)
        if form.is_valid():
            user = form.login()
            if user is None:
                form.add_login_error()
            else:
                auth.login(req, user)
                return redirect('/')
    else:
        form = forms.Login()

    return render(req, 'rfixuser/login.html', {'form': form})
