from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)


