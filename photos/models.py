from django.db import models
from datetime import datetime
from django.conf import settings
from users.models import Account

# Create your models here.
class Tag(models.Model):

    tag_name = models.CharField(max_length=20, default='')
    def __unicode__(self):
        return self.tag_name

class Photo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(default=None)
    #related_name can reverse foreign krey to one-to-many
    owner = models.ForeignKey(Account, related_name='photos')
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    Flickr_vote = models.IntegerField(default=0)
    FB_vote = models.IntegerField(default=0)
    upload_time = models.DateTimeField(default=datetime.now, blank=False, null=False)
    image = models.ImageField(upload_to='uploads/images')


    def __unicode__(self):
        return self.title
