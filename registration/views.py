from django.shortcuts import render
from django.views import generic
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_date')
    template_name = 'index.html'
    paginate_by = 10
