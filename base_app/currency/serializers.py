from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=False)
    
    class Meta:
        model = Currency
        fields = ('pk', 'name', 'symbol', 'market_cap', 'price')
