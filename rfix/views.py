from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as tr
from rfix.page import models


def guest(req):
    template = get_template('guest.html')
    context = {
        'page': models.Page.guest_default(),
        'header': tr('RFIX'),
        'subheader': tr('lightweight bug tracker'),
        'email': 'rasmadeus@gmail.com',
        'links': (
            {'name': tr('Support'), 'href': '/support'},
            {'name': tr('Login'), 'href': '/users/login'},
        )
    }
    return HttpResponse(template.render(context, req))


def index(req):
    return redirect(req.user) if req.user.is_authenticated() else guest(req)
