from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from rfix.project import views

urlpatterns = [
    url(
        r'^(?P<slug>[-\w]+)/$',
        login_required(views.ProjectDetail.as_view()),
        name='project_detail'
    ),
]
