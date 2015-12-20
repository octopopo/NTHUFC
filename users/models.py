#-*- encoding=UTF-8 -*-
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #activation_key = models.CharField(max_length=40, blank=True)
    # default active time is 15 minutes
    #active_time = models.DateTimeField(default=lambda: datetime.now() + timedelta(minutes=15))
    current_student = models.BooleanField(default=True)
    def __unicode__(self):
        return self.user.username
'''

class Account(models.Model):
    username = models.CharField(max_length=20, default='', unique=True)
    nickname = models.CharField(max_length=20, default='', unique=True)

    TEACHER = 'TE'
    STUDENT = 'ST'
    OFFICER = 'OF'
    ALUMNUS = 'AL'
    IDENTITY_CHOICES = (
        (ALUMNUS, '校友'),
        (OFFICER, '職員'),
        (STUDENT, '學生'),
        (TEACHER, '教師')
    )

    identity = models.CharField(max_length=2, choices=IDENTITY_CHOICES, default=None)
    major = models.CharField(max_length=20, default='', blank=True, null=True)
    email = models.EmailField(max_length=250, unique=True)
    cellphone = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Invalid number', code='Invalid number')])
    def __unicode__(self):
        return self.username
