from django.shortcuts import render
from .models import Currency
from .tasks import update_database


def currency_list(request):
    
    update_database.delay() # celery task: update db
    currencies = Currency.objects.all()
    page = 'currency'
    return render(request, 'currency/list.html', locals())
