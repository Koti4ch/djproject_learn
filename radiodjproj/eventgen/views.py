from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail

from eventgen.models import Event, Comment
from eventgen.forms import EmailEventForm, CommentForm
# Create your views here.

def infopage(request):
    return render(request, 'eventgen/event/machineinfo.html')

def event_share_by_post(request, event_id):
    # Get event by index
    event = get_object_or_404(Event, id=event_id, status='active')
    sent = False
    if request.method == 'POST':
        # Form was saved
        form = EmailEventForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # ...try to send mail
            event_url = request.build_absolute_uri(event.get_absolute_url())
            subject = '{},({}) recomends you reading "{}"'.format(cd['name'], cd['email'], event.title)
            message = f'Read "{event.title}" at {event_url}\n\n{cd["name"]}\'s comments: {cd["comments"]}'
            send_mail(subject, message, 'admin@admin.tv', [cd['to']])
            sent = True
        else:
            form = EmailEventForm()
    else:
        form = EmailEventForm()
    return render(request, 'eventgen/event/eventshare.html', {'event': event, 'form': form, 'sent': sent})

class EventsListView(ListView):
    queryset = Event.actived.all()
    context_object_name = 'events'
    paginate_by = 3
    template_name = 'eventgen/event/all_active.html'

# LIKE AS EventsListView, but method

# def active_events_list(request):
#     object_list = Event.actived.all()
#     paginator = Paginator(object_list, per_page=3)
#     page = request.GET.get('page')
#     pagi = True if paginator.num_pages else False
#
#
#     try:
#         events = paginator.page(page)
#     except PageNotAnInteger:
#         events = paginator.page(1)
#     except EmptyPage:
#         events = paginator.page(paginator.num_pages)
#
#     return render(request, 'eventgen/event/all_active.html', {'activeevents': events, 'page': page, 'pagi': pagi})

def event_detail(request, year, month, day, event):
    current_event = get_object_or_404(Event, slug_field=event, status='active', activated__year=year,
                                      activated__month=month, activated__day=day)
    comments = current_event.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.event = current_event
            new_comment.save()
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'eventgen/event/event_detail.html', {'event': current_event,
                                                                'comments': comments,
                                                                'new_comment': new_comment,
                                                                'comment_form': comment_form,
                                                                })