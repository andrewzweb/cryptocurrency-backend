from django.shortcuts import render


def home(request):
    return render(request, 'home/entrypoint.html')

def landing(request):
    return render(request, 'home/landing.html')
