from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rfix.rfixuser import views

urlpatterns = [
    url(r'^login', views.login),
    url(
        r'^(?P<slug>[-\w]+)/$',
        login_required(views.RfixUserDetail.as_view()),
        name='rfixuser_detail'
    ),
]
