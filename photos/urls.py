from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.photos, name='photos'),
    url(r'^upload/(?P<photo_id>[0-9]+)/', views.upload, name='upload'),
    url(r'^show/',views.show, name='show'),
    url(r'^ajax_post_comment/', views.ajax_post_comment, name='ajax_post_comment'),
    url(r'^ajax_post_like/', views.ajax_post_like, name='ajax_post_like'),
)