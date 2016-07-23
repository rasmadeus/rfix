from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static  import static

from django.contrib import admin
admin.autodiscover()

from rfix.spage import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
