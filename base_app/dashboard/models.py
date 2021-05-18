from django.db import models

from currency.models import Currency
from account.models import Account

class Dashboard(models.Model):
    '''dashboard '''
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, blank=True)
    currency = models.ManyToManyField(Currency, blank=True)
