from django.db import models
from datetime import datetime
from django.conf import settings
from users.models import Account

# Create your models here.
class Tag(models.Model):

    tag_name = models.CharField(max_length=20, default='')
    tag_count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.tag_name

class LocationMarker(models.Model):
    location_text = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=18, decimal_places=15);
    longitude = models.DecimalField(max_digits=18, decimal_places=15);

    def __unicode__(self):
        return self.location_text;

class Photo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(default=None)
    #related_name can reverse foreign krey to one-to-many
    owner = models.ForeignKey(Account, related_name='photos')
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    location_marker = models.ForeignKey(LocationMarker)
    flickr_photo_id = models.CharField(max_length=50)
    facebook_post_id = models.CharField(max_length=50)
    upload_time = models.DateTimeField(default=datetime.now, blank=False, null=False)
    image = models.ImageField(upload_to='uploads/images')

    def __unicode__(self):
        return self.title
