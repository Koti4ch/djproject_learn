from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class ActivatedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


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

    def get_absolute_url(self):
        return reverse('eventgen:event_detail', args=[self.created.year, self.created.month, self.created.day, self.slug_field])

    objects = models.Manager()
    actived = ActivatedManager()
