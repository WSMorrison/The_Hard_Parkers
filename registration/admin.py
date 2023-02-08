from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    title = ('Event Date')
    list_filter = ('event_date',)
