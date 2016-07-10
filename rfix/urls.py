from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from rfix.spage import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]