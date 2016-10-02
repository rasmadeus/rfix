from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as tr
from rfix.project.models import Project


def _links_auth(req):
    return {
        'links': (
            {
                'name': tr('Projects'),
                'href': '#',
                'sublinks': (
                    {'name': project.name, 'href': project.get_absolute_url()}
                    for project in Project.objects.all()
                ),
            },
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
    has_req_user = req.user.is_authenticated
    return _links_auth(req) if has_req_user else _links_guest(req)


def index(req):
    return redirect(req.user) if req.user.is_authenticated() else _guest(req)
