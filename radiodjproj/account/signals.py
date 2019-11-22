from django.contrib.auth.models import User
from django.conf import settings
from account.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_pic(sender, instance, created, **kwards):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_user_pic(sender, instance, **kwargs):
    instance.userprofile.save()
