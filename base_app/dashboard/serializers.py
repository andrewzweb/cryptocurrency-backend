from rest_framework import serializers
from .models import Dashboard
from account.models import Account
from currency.serializers import CurrencySerializer
from account.serializers import AccountSerializer
from currency.models import Currency

class DashboardSerializer(serializers.ModelSerializer):
    ''' dashboard serializers '''
    
    currency = CurrencySerializer(many=True, read_only=False)
    account = AccountSerializer(read_only=True)
    
    class Meta:
        model = Dashboard
        fields = [
            'pk',
            'account',
            'currency',
        ]

    def create(self, validated_data):
        currency_data = validated_data.pop('currency')
        dashboard = Dashboard.objects.create(**validated_data)
        for currency in currency_data:
            item = Currency.objects.get(**currency)
            dashboard.currency.add(item)
        return dashboard

    def update(self, instance, validated_data):
        print('all data', validated_data)
        instance.pk = validated_data.get('pk', instance.pk)
        instance.account = validated_data.get('account', instance.account)
        currency_data = validated_data.get('currency', instance.currency)
        print('all data', currency_data)
        for currency in currency_data:
            item = Currency.objects.get(pk= currency['pk'])
            instance.currency.add(item)
        
        instance.save()
        return instance
