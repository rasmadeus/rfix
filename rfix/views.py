from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from rfix.page import models


def guest(req):
    template = get_template('guest.html')
    context = {'page': models.Page.guest_default()}
    return HttpResponse(template.render(context, req))


def index(req):
    return redirect(req.user) if req.user.is_authenticated() else guest(req)
