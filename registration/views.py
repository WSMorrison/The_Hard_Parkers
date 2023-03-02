from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event, Siteuser


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_date')
    template_name = 'index.html'
    paginate_by = 10


class EventView(View):

    def get(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(
            request,
            'eventview.html',
            {'event': event}
        )


class EventReg(generic.ListView):
    model = Event
    template_name = 'eventreg.html'
