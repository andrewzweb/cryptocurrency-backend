from django.contrib import admin
from .models import Dashboard


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    ''' dashboard admin '''
    filter_horizontal = ('currency',)

#    inlines = [
#        CurrencyInline,
#    ]
