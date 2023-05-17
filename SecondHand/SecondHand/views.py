from django.http import HttpResponse
from django.shortcuts import render

def main (request):
    return  render(request, 'main.html')

def Add_data(request):
    return HttpResponse('Add data page')

def Serch_New_Arrivals(request):
    return HttpResponse('Search new arrivalse')

