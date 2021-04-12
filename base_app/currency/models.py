from django.db import models
from account.models import Account

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

    def __str__(self):
        return 'Currency: {}'.format(self.name)


class Dashboard(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    currency = models.ManyToManyField(Currency)

    def __str__(self):
        return "Dashboard: {}".format(self.account.name)
