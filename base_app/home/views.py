from django.shortcuts import render


def home(request):
    page = 'home'
    return render(request, 'home/entrypoint.html', locals())

def landing(request):
    return render(request, 'home/landing.html')
