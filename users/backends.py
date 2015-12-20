from django.contrib.auth.models import User
from users.models import Account

class EmailAuthBackend(object):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair rather than
    a username/password pair.
    """

    def authenticate(self, username=None, email=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(username=username, email=email)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
