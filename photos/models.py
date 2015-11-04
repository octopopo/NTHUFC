from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.

class Photo(models.Model):
    title = models.TextField(default=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    #upload_time = models.DateTimeField(default=datetime.now)
    Flickr_vote = models.IntegerField()
    FB_vote = models.IntegerField()
    def __unicode__(self):
        return str(self.title)
