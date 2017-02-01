from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<foodgroups>[-@.\w]+)$', views.detail, name='detail'),
]
