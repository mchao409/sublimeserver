from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OnetoOneField(settings.AUTH_USER_MODEL)
    # bio = models.TextField(max_length=500, blank=True)
    dropbox_token = models.CharField(max_length=200, blank=True)
    googledrive_token = models.CharField(max_length=200,blank=True)
    googledrive_refresh = models.CharField(max_length=200, blank=True)

    # birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

