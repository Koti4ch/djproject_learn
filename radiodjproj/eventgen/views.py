from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from eventgen.models import Event

# Create your views here.
def active_events_list(request):
    object_list = Event.actived.all()
    paginator = Paginator(object_list, per_page=3)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    return render(request, 'eventgen/event/all_active.html', {'activeevents': events, 'page': page})

def event_detail(request, year, month, day, event):
    current_event = get_object_or_404(Event, slug_field=event, status='active', activated__year=year,
                                      activated__month=month, activated__day=day)
    return render(request, 'eventgen/event/event_detail.html', {'event': current_event})