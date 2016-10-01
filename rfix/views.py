from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as tr


def guest(req):
    template = get_template('guest.html')
    context = {
        'header': tr('RFIX'),
        'subheader': tr('lightweight bug tracker'),
        'links': (
            {'name': tr('Support'), 'href': '/support'},
            {'name': tr('Login'), 'href': '/users/login'},
        )
    }
    return HttpResponse(template.render(context, req))


def index(req):
    return redirect(req.user) if req.user.is_authenticated() else guest(req)
