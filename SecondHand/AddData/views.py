from django.http import HttpResponse
from django.shortcuts import render
from .models import Shop, Arrival_of_goods, Special_offer, Chain
from .forms import CreateChainForm
from django.views.generic import CreateView

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