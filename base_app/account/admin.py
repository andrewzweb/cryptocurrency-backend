from django.contrib import admin

from account.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    ''' account admin '''
    list_display = (
        'user',
        'picture',
        'name',
    )
