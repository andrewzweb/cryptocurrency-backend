from django.db import models

from currency.models import Currency
from account.models import Account

class Dashboard(models.Model):
    '''dashboard '''
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    currency = models.ManyToManyField(Currency)

    def __str__(self):
        return "Dashboard: {}".format(self.account.name)
