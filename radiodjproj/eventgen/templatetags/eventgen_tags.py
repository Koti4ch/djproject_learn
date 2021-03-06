from django import template
from django.db.models import Count
from eventgen.models import Event

####  CUSTOM TAGs HERE
register = template.Library()

@register.simple_tag
def total_events():
    return Event.actived.count()

@register.simple_tag
def get_most_commented(count=1):
    return Event.actived.annotate(total_commens=Count('comments')).order_by('-total_commens')[:count]