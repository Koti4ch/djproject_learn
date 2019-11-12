from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('active', 'Active'),
    )

    title = models.CharField(max_length=250)
    slug_field = models.SlugField(max_length=250, unique_for_date='activated')
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='radio_events')
    eventtext = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    activated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-activated',)

    def __str__(self):
        return self.title

