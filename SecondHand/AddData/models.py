from django.db import models
import datetime

class Chain(models.Model):
    id_chain = models.IntegerField(primary_key=True, blank=False, default=None)
    name_of_chain = models.CharField(max_length=50, blank=False, default=None)
    description = models.TextField(blank=False, default=None)
    logo_chain = models.FileField(upload_to='img/')

class Shop(models.Model):
    id_shop = models.IntegerField(primary_key=True, blank=False, default=None)
    country = models.CharField(max_length=50, blank=False, default=None)
    city = models.CharField(max_length=50, blank=False, default=None)
    store_address = models.CharField(max_length=50, blank=False, default=None)
    description = models.TextField(blank=False, default=None)
    opening_time_mon = models.TimeField(default=datetime.time(00,00,00))
    closing_time_mon = models.TimeField(default=datetime.time(00,00,00))

    opening_time_tues = models.TimeField(default=datetime.time(00,00,00))
    closing_time_tues = models.TimeField(default=datetime.time(00,00,00))

    opening_time_wed = models.TimeField(default=datetime.time(00,00,00))
    closing_time_wed = models.TimeField(default=datetime.time(00,00,00))

    opening_time_thur = models.TimeField(default=datetime.time(00,00,00))
    closing_time_thur = models.TimeField(default=datetime.time(00,00,00))

    opening_time_fri = models.TimeField(default=datetime.time(00,00,00))
    closing_time_fri = models.TimeField(default=datetime.time(00,00,00))

    opening_time_sat = models.TimeField(default=datetime.time(00,00,00))
    closing_time_sat = models.TimeField(default=datetime.time(00,00,00))

    opening_time_sun = models.TimeField(default=datetime.time(00,00,00))
    closing_time_sun = models.TimeField(default=datetime.time(00,00,00))

    foto_store = models.FileField(upload_to='img/')
    chain = models.ManyToManyField(Chain)

class Arrival_of_goods(models.Model):
    id_arrival = models.IntegerField(primary_key=True, blank=False, default=None)
    name_of_arrival = models.CharField(max_length=50, blank=False, default='Новое поступление')
    description = models.TextField()
    date = models.DateTimeField(blank=False, default=None)
    shop = models.ManyToManyField(Shop)

class Special_offer(models.Model):
    id_offer = models.IntegerField(primary_key=True, blank=False, default=None)
    name_of_offer = models.CharField(max_length=50, blank=False, default='Новое поступление')
    description = models.TextField()
    start_date = models.DateTimeField(blank=False, default=None)
    finish_date = models.DateTimeField(blank=False, default=None)
    shop = models.ManyToManyField(Shop)



# Create your models here.
