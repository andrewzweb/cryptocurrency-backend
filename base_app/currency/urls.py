from django.urls import path, include
from . import views

app_name = 'currency'

urlpatterns = [
    path('', views.currency_list, name='list'),
]
