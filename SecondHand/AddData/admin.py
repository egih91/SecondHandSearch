from django.contrib import admin
from.models import Shop, Arrival_of_goods, Chain, Buyer_category, Discount, Fix_price, Stock, Record
from django_ymap.admin import YmapAdmin

class RecordAdmin(YmapAdmin, admin.ModelAdmin):
    pass

admin.site.register(Record, RecordAdmin)
admin.site.register(Shop)
admin.site.register(Arrival_of_goods)
admin.site.register(Chain)
admin.site.register(Fix_price)
admin.site.register(Stock)
admin.site.register(Buyer_category)
admin.site.register(Discount)







# Register your models here.
