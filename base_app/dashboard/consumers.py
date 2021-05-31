import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from currency.models import Currency


class CurrencyConsumer(WebsocketConsumer):
    '''
    Consumer currency
    '''
        
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print('Socket get : %s' % self.room_name)
        self.room_group_name =  self.room_name #'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    
    def fetch_currency(self, data):
        print('S: fetch, data', data)

        currency_name = data['currency']
        item = Currency.objects.get(name=currency_name)
        data = {
            'id': item.pk,
            'name': item.name,
            'symbol': str(item.symbol),
            'price': str(item.price),
            'market_cap': str(item.market_cap)
        }
        self.send_data('fetch', data)
            
    commands = {
        'fetch_currency': fetch_currency,
    }

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[ data['command'] ](self, data)

    def send_data(self, type_message, data):
        self.send(text_data=json.dumps({
            'type': type_message,
            'data': data
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
