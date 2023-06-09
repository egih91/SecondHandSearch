from django import forms

from .models import Chain, Shop, Arrival_of_goods, Discount
from django.forms import ModelForm

class CreateChainForm(ModelForm):
    class Meta:
        model = Chain
        fields = '__all__'

class CreateShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'

class CreateArrivalForm(ModelForm):
    class Meta:
        model = Arrival_of_goods
        fields = '__all__'

class CreateDiscountForm(ModelForm):
    class Meta:
        model = Discount
        fields = '__all__'



