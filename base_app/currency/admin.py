''' admin product '''

from django.contrib import admin
from .models import Currency, Dashboard


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


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    ''' dashboard admin '''
    filter_horizontal = ('currency',)

#    inlines = [
#        CurrencyInline,
#    ]
