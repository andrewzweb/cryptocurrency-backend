# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/currency/(?P<room_name>\w+)/$', consumers.CurrencyConsumer.as_asgi()),
]
