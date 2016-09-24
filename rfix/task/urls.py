from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rfix.task import views

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        login_required(views.TaskDetail.as_view()),
        name='task_detail'
    ),
]
