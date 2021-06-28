from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    creates profile when a user is created
    '''
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''
    saves profile of the User instance
    '''
    instance.profile.save()
