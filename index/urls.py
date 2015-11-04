from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
)
