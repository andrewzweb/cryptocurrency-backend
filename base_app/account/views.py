from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from dashboard.models import Dashboard
from .models import Account

def login_account(request):
    ''' login account '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('home:home'))

    return render(request, 'account/login.html', locals())


def logout_account(request):
    ''' logout account '''
    logout(request)
    return redirect(reverse('home:home'))

def dashboard(request):
    ''' dashboard account '''
    page = 'dashboard'
    if request.user.is_anonymous:
        pass
    else:
        try:
            account = Account.objects.get(user=request.user)
            dashboard = Dashboard.objects.get(account=account)
        except:
            redirect(reverse('account:login'))
    return render(request, 'account/dashboard.html', locals())
