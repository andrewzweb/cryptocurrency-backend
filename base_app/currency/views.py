from django.shortcuts import render


def currency_list(request):
    return render(request, 'currency/list.html')
