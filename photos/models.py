#coding=utf-8

from django.db import models
from django.utils import timezone
from django.conf import settings
from users.models import Account
from locationMarker.models import Marker
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
class Tag(models.Model):

    tag_name = models.CharField(max_length=20, default='')
    tag_count = models.IntegerField(default=0)
    update_time = models.DateTimeField(default=timezone.now(), blank=False)
    def __unicode__(self):
        return self.tag_name
    
    #比較某個詞跟這個標籤相似性
    def similarity(self, word):
        score = 0
        print type(self.tag_name)
        print type(word)
        uni_tag = self.tag_name
        uni_word = word
        for i in range(1,len(uni_word)+1):
            if i > len(uni_tag):
                continue
            for j in range(len(uni_word)-i+1):
                if uni_tag.find(uni_word[j:j+i]) > -1:
                    score += i
        return score

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
    tags = models.CharField(max_length=32, default='tag1',validators=[RegexValidator(regex='^[^ ]{1,10}( [^ ]{1,10}){0,2}$',message='You can only enter at most 3 tags and seperate any 2 tags with a space.')])
    location_marker = models.ForeignKey(Marker,blank=False, default=Marker.objects.all()[0])
    flickr_photo_id = models.CharField(max_length=50,blank=True)
    flickr_photo_url = models.URLField(max_length=100,blank=True)
    facebook_post_id = models.CharField(max_length=50,blank=True)
    upload_time = models.DateTimeField(default=timezone.now(), blank=False, null=False)
    image = models.ImageField(upload_to='uploads/images')

    def __unicode__(self):
        return self.title

    def getTagString(self):
        tagString = ''
        for tag in self.tags:
            tagString += tag.tag_name;
        return tagString;
