from django.db import models
from asgiref.sync import async_to_sync # for WebSocket
from channels.layers import get_channel_layer # for WebSocket

channels_layer = get_channel_layer()


class Currency(models.Model):
    ''' currency '''
    name = models.CharField(max_length=30)
    symbol = models.CharField(max_length=10)
    market_cap = models.BigIntegerField(default=0)
    price = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        blank=True
     )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-price"]

    def save(self, *args, **kwargs):
        super(Currency, self).save(*args, **kwargs)
        # send update to socket
        try:
            #print(self)
            async_to_sync(channels_layer.group_send)(self.name, {
                'type': 'fetch_currency',
                'currency': self.name
            })
        except: pass
