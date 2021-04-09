from django.urls import path
from . import views

app_name = 'currency'

urlpatterns = [
    path('', views.currency_list, name='list'),
 ]
