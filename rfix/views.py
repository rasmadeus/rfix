from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as tr


def _links_auth(req):
    return {
        'links': (
            {'name': tr('Support'), 'href': '/support'},
            {'name': tr('Login'), 'href': '/users/login'},
        )
    }


def _links_guest(req):
    return {
        'links': (
            {'name': tr('Login'), 'href': '/login'},
        )
    }


def _guest(req):
    template = get_template('guest.html')
    context = {
        'header': tr('RFIX'),
        'subheader': tr('lightweight bug tracker'),
    }
    return HttpResponse(template.render(context, req))


def links(req):
    return _links_auth(req) if req.user.is_authenticated() else _links_guest(req)


def index(req):
    return redirect(req.user) if req.user.is_authenticated() else _guest(req)
