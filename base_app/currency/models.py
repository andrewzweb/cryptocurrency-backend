from django.db import models
from asgiref.sync import async_to_sync # for WebSocket
from channels.layers import get_channel_layer # for WebSocket
import logging

logger = logging.getLogger(__name__)
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

    #def __str__(self):
    #    return 'Currency: {}'.format(self.name)

    def save(self, *args, **kwargs):
        super(Currency, self).save(*args, **kwargs)
        # send update to socket
        try:
            logger.debug('[ ] Try send to ws message ...')
            async_to_sync(channels_layer.group_send)('chat_dashboard', {
                'type': 'update_dashboard',
                'message': 'text'
            })
            logger.debug('[+] Send to ws message ...')
        except:
            logger.debug('[-] Error send to ws message ...')
