from django.conf.urls import url
from rfix.rfixuser import views

urlpatterns = [
    url(
        r'^(?P<slug>[-\w]+)/$',
        views.RfixUserDetail.as_view(),
        name='rfixuser_detail'
    ),
]
