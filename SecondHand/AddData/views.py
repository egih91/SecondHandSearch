from django.http import HttpResponse
from django.shortcuts import render
from .models import Shop, Arrival_of_goods, Chain, Discount, Buyer_category, Fix_price, Stock
from .forms import CreateChainForm, CreateShopForm, CreateArrivalForm, CreateDiscountForm
from django.views.generic import CreateView
import datetime

def Add_store (request):
    return  render(request, 'main.html')

def Show_story(request):
    shops = Shop.objects.all()
    events = Arrival_of_goods.objects.all()
    context = {'shops':shops, "events":events}
    return render(request, 'show.html',context)

class CreateChain(CreateView):
    # Модель куда выполняется сохранение
    model = Chain
    # Класс на основе которого будет валидация полей
    form_class = CreateChainForm
    # Выведем все существующие записи на странице
    extra_context = {'Chains': Chain.objects.all()}
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'chain.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    success_url = ''

class ShowChain(CreateView):
    model = Chain
    form_class = CreateChainForm
    extra_context = {'Chains': Chain.objects.all()}
    template_name = 'showchain.html'

class ShowShop(CreateView):
    model = Shop
    form_class = CreateShopForm
    extra_context = {'Shops': Shop.objects.all()}
    template_name = 'showshop.html'

class ShowArrival(CreateView):
    model = Arrival_of_goods
    form_class = CreateArrivalForm
    chain = Chain.objects.all()
    arrivals = Arrival_of_goods.objects.filter( date__date__gte= datetime.datetime.today()).order_by('date')
    extra_context = {'Arrivals': arrivals, 'Chains':chain}
    template_name = 'showarrival.html'

def Show_Arrival_Filtred_By_Chain(request, pk):#Фильтрация завозов по сетям
    shop_list = Shop.objects.filter(chain = pk)
    arrivals = Arrival_of_goods.objects.filter( date__date__gte= datetime.datetime.today()).filter(shop__in = shop_list).order_by('date')
    context = {
        'Arrivals': arrivals,
    }
    return render(request, 'showarrival.html',context)

def Show_Arrival_Filtred_By_Shop(request, pk):#Фильтрация завозов по магазинам
    arrivals = Arrival_of_goods.objects.filter( date__date__gte= datetime.datetime.today()).filter(shop = pk).order_by('date')
    context = {
        'Arrivals': arrivals,
    }
    return render(request, 'showarrival.html',context)

class ShowDiscount(CreateView):#Выводит скидки для всех покупателей
    model = Discount
    form_class = CreateDiscountForm
    discount = Discount.objects.filter(start_date__date__gte = datetime.datetime.today()).order_by('start_date')
    byer_category = Buyer_category.objects.all()
    extra_context = {'Discount': discount, 'Byer_caterory': byer_category}
    template_name = 'showdiscount.html'

class ShowDiscountRetiree(CreateView):# Выводит скидки только для пенсионеров
    model = Discount
    form_class = CreateDiscountForm
    discount = Discount.objects.filter(start_date__date__gte=datetime.datetime.today()).filter(buyer='Пенсионерам').order_by('start_date')#
    byer_category = Buyer_category.objects.all()
    extra_context = {'Discount': discount, 'Byer_caterory': byer_category}
    template_name = 'showdiscount.html'

class ShowDiscountDisabled(CreateView):# Выводит скидки только для инвалидов
    model = Discount
    form_class = CreateDiscountForm
    discount = Discount.objects.filter(start_date__date__gte=datetime.datetime.today()).filter(buyer='Инвалидам').order_by('start_date')#
    byer_category = Buyer_category.objects.all()
    extra_context = {'Discount': discount, 'Byer_caterory': byer_category}
    template_name = 'showdiscount.html'


class ShowDiscountParticipant(CreateView):# Выводит скидки только для участников дисконтных программ
    model = Discount
    form_class = CreateDiscountForm
    discount = Discount.objects.filter(start_date__date__gte=datetime.datetime.today()).filter(buyer='По дисконтным картам').order_by('start_date')#
    byer_category = Buyer_category.objects.all()
    extra_context = {'Discount': discount, 'Byer_caterory': byer_category}
    template_name = 'showdiscount.html'