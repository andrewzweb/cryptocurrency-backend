import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from currency.models import Currency
from currency.serializers import CurrencySerializer

class TestCurrencySerializers:
    '''test serializers'''

    def test_currency_serializers(self):

        mixer.cycle(5).blend('currency.Currency')
        data = Currency.objects.all()

        #print(dir(CurrencySerializer))
        serializer_all_items = CurrencySerializer(data, many=True)
        #print('all', serializer_all_items)
        serializers_item = CurrencySerializer(
            Currency.objects.first()
        )
        #print('item', serializers_item)
        assert serializers_item.data in serializer_all_items.data
