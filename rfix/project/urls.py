from django.conf.urls import url
from rfix.project import views

urlpatterns = [
    url(
        r'^(?P<slug>[-\w]+)/$',
        views.ProjectDetail.as_view(),
        name='project_detail'
    ),
]
