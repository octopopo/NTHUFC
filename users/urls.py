from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.users, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
)