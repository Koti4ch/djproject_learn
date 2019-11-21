from django import template
from django.db.models import Count
from eventgen.models import Event
import os

####  CUSTOM TAGs HERE
register = template.Library()

@register.simple_tag
def total_events():
    return Event.actived.count()

@register.simple_tag
def get_most_commented(count=1):
    return Event.actived.annotate(total_commens=Count('comments')).order_by('-total_commens')[:count]

@register.simple_tag
def localsystem_info():
    system_info = dict()
    infolist = ['username', 'userdomain', 'computername', 'os']
    for _ in infolist:
        if os.getenv(_):
            system_info[_] = (os.getenv(_))
    return system_info