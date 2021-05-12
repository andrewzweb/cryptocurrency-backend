''' admin product '''

from django.contrib import admin
from .models import Currency


@admin.register(Currency)
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


class CurrencyInline(admin.TabularInline):
    model = Currency
