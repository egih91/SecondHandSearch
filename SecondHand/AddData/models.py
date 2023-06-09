from django.db import models
import datetime
from django_ymap.fields import YmapCoord


class Record(models.Model):
    title = models.CharField(max_length=200)
    address = YmapCoord(max_length=200, start_query=u'Россия', size_width=500, size_height=500)
    alternative_address = YmapCoord(max_length=200, start_query=u'Австралия', size_width=500, size_height=500)

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

class Buyer_category (models.Model):
    name_of_buyer_category = models.CharField(primary_key=True, max_length=50, blank=False)
    description = models.TextField()

class Discount (models.Model):
    id_discount = models.IntegerField(primary_key=True, blank=False, default=None)
    discount = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    start_date = models.DateTimeField(blank=False, default=None)
    buyer = models.ManyToManyField(Buyer_category)
    shop = models.ManyToManyField(Shop)

class Stock (models.Model):
    id_stock = models.IntegerField(primary_key=True, blank=False, default=None)
    stock = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    date = models.DateTimeField(blank=False, default=None)
    buyer = models.ManyToManyField(Buyer_category)
    shop = models.ManyToManyField(Shop)

class Fix_price (models.Model):
    id_fix_price = models.IntegerField(primary_key=True, blank=False, default=None)
    price = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    date = models.DateTimeField(blank=False, default=None)
    buyer = models.ManyToManyField(Buyer_category)
    shop = models.ManyToManyField(Shop)



# Create your models here.
