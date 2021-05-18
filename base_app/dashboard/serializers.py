from rest_framework import serializers
from .models import Dashboard
from account.models import Account
from currency.serializers import CurrencySerializer
from account.serializers import AccountSerializer


class DashboardSerializer(serializers.ModelSerializer):

    currency = CurrencySerializer(many=True, read_only=True)
    account = AccountSerializer(read_only=True)
    
    class Meta:
        model = Dashboard
        fields = [
            'pk',
            'account',
            'currency',
        ]
