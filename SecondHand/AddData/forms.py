from django import forms

from .models import Chain, Shop, Special_offer, Arrival_of_goods
from django.forms import ModelForm

class CreateChainForm(ModelForm):
    class Meta:
        model = Chain
        fields = '__all__'



