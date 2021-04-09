''' admin product '''

from django.contrib import admin
from . import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    ''' product admin '''
    list_display = (
        'name',
        'symbol',
        'market_cap',
        'price'
    )
    list_editable = (
        'market_cap',
        'price'
    )
    search_fields = ('name', 'symbol')
    list_filter = ('updated', 'created')
