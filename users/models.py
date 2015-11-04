from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    '''
    activation_key = models.CharField(max_length=40, blank=True)
    # default active time is 15 minutes
    active_time = models.DateTimeField(default=lambda: datetime.now() + timedelta(minutes=15))
    '''
    current_student = models.BooleanField(default=True)
    def __unicode__(self):
        return self.user.username
