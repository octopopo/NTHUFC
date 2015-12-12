from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.photos, name='photos'),
    url(r'^upload/(?P<photo_id>[0-9]+)', views.upload, name='upload'),
)