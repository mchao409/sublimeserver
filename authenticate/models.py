from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OnetoOneField(settings.AUTH_USER_MODEL)
    # bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

# @receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

