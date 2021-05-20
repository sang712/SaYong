from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.fields import CharField


class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    object_type = models.IntegerField()
    object_pk = models.IntegerField()
    action_type = models.IntegerField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)