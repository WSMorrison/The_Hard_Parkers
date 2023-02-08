from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_name = models.CharField(max_length=50, unique=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    event_date_reg_close = models.DateTimeField()
    event_location = models.CharField(max_length=100)
    event_location_url = models.URLField(max_length=200)
    number_cars = models.IntegerField(default=1)
    feature_cars = models.BooleanField(default=False)
    number_feature_cars = models.IntegerField(default=0)
    event_description = models.TextField()

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.event_name


class Car(models.Model):
    car_name = models.CharField(max_length=20, unique=True)
    car_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car_year = models.IntegerField()
    car_make = models.CharField(max_length=20)
    car_model = models.CharField(max_length=50)
    car_origin = models.CharField(max_length=10)
    car_modifications = models.CharField(max_length=200)
    feature_consideration = models.BooleanField(default=False)
    feature_approved = models.BooleanField(default=False)


class Siteuser(models.Model):
    site_user = ForeignKey(User, on_delete=models.CASCADE)
    event_organizer = models.BooleanField(default=False)
