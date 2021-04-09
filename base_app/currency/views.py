from django.shortcuts import render

from .models import Currency

def currency_list(request):
    currencies = Currency.objects.all()
    page = 'currency'
    return render(request, 'currency/list.html', locals())
