from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """User profile model"""
    user = models.OneToOneField(User, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_images')
    location = models.CharField(max_length=100)
    google_location_lat = models.FloatField()
    google_location_long = models.FloatField()

    def __unicode__(self):
        return self.user.first_name + " profile"
    

