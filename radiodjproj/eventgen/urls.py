from django.urls import path
from eventgen import views as eventsviews

app_name = 'eventgen'

urlpatterns = [
    path('', eventsviews.active_events_list, name='events_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:event>/', eventsviews.event_detail, name='event_detail'),
]