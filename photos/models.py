from django.db import models
from datetime import datetime
from django.conf import settings
from users.models import Account
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

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
    tags = models.CharField(max_length=32, validators=[RegexValidator(regex='^[^ ]{1,10}( [^ ]{1,10}){0,2}$',message='You can only enter at most 3 tags and seperate any 2 tags with a space.')])
    location_marker = models.ForeignKey(LocationMarker)
    flickr_photo_id = models.CharField(max_length=50,blank=True)
    flickr_photo_url = models.URLField(max_length=100,blank=True)
    facebook_post_id = models.CharField(max_length=50,blank=True)
    upload_time = models.DateTimeField(default=datetime.now, blank=False, null=False)
    image = models.ImageField(upload_to='uploads/images')

    def __unicode__(self):
        return self.title

    def getTagString(self):
        tagString = ''
        for tag in self.tags:
            tagString += tag.tag_name;
        return tagString;
