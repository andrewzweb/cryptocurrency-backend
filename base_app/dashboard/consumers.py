import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from currency.models import Dashboard


class DashboardConsumer(WebsocketConsumer):

    def fetch_dashboard(self, data):
        print('fetch')
        pass

    def update_dashboard(self, data):
        content = {
            'dashboard': self._get_data_from_dashboard()
        }
        self.send_dashboard(content)
        print('update')

    commands = {
        'fetch_dashboard': fetch_dashboard,
        'update_dashboard': update_dashboard
    }

        
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name =  'chat_dashboard' #'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[ data['command'] ](self, data)

    def send_dashboard(self, data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'send_data',
                'message':data
            }
        )
            
    def send_data(self, event):
        data = event['message']
        self.send(text_data=json.dumps({
            'type':'dashboard',
            'dashboard':data
        }))

    def _get_data_from_dashboard(self, user=None):
        dashboard = Dashboard.objects.first().currency.all()
        result = []
        for item in dashboard:
            result.append(
                {
                    "name":item.name,
                    "symbol":item.symbol,
                    "market":str(item.market_cap),
                    "price":str(item.price)
                }
            )
        return result
