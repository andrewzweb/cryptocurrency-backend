import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from currency.models import Dashboard


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name =  'chat_dashboard' #'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'update_currency',
                'message': message
            }
        )

    # Receive message from room group
    def update_currency(self, event):

        dashboard = Dashboard.objects.first().currency.all()
        result = []
 
        for item in dashboard:
            result.append(
                {
                    'name': item.name,
                    'symbol': item.symbol,
                    'market': str(item.market_cap),
                    'price': str(item.price),
                }
            )
        currency = json.dumps(result)
        
        self.send(text_data=json.dumps({
            'currency': currency
        }))
