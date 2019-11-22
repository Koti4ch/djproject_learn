from django.db import models
from django.conf import settings

from PIL import Image

# Create your models here.

class UserProfile(models.Model):
    GENDERS = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('secret', 'Don\'t say')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDERS, default='secret', max_length=10)
    photo = models.ImageField(upload_to='user_avas/%Y/%m/%d/', default='user_avas/defuserpic.png')

    def __str__(self):
        return f'Profile for user {self.user.username}'

    def save(self):
        super().save()
        with Image.open(self.photo.path) as userava:
            if userava.height > 256 or userava.width > 256:
                resize = (256, 256)
                userava.thumbnail(resize)
                userava.save(self.photo.path)