from rest_framework import serializers
from .models import Dashboard
from account.models import Account
from currency.serializers import CurrencySerializer
from account.serializers import AccountSerializer
from currency.models import Currency

class DashboardSerializer(serializers.ModelSerializer):

    # currency = serializers.PrimaryKeyRelatedField(many=True, queryset=Currency.objects.all())
    currency = serializers.StringRelatedField(many=True, queryset=Currency.objects.all())
    account = AccountSerializer(read_only=True)
    
    class Meta:
        model = Dashboard
        fields = [
            'pk',
            'account',
            'currency',
        ]

    def update(self, instance, validated_data):
        instance.pk = validated_data.get('pk', instance.pk)
        print('pk', instance.pk)
        instance.account = validated_data.get('account', instance.account)
        print('account', instance.account)

        print('currency', validated_data.get('currency', instance.currency))
        instance.currency.set(validated_data.get('currency', instance.currency) )
        print('currency', instance.currency)
        instance.save()
        return instance
