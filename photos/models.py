from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(default=None)
    #related_name can reverse foreign krey to one-to-many
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photos')
    #upload_time = models.DateTimeField(default=datetime.now)
    Flickr_vote = models.IntegerField()
    FB_vote = models.IntegerField()
    def __unicode__(self):
        return str(self.title)
