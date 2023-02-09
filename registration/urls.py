from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<str:event_name>/', views.EventView.as_view(), name='event_view'),
]
