import pytest
from ..utils import get_all_currency_data, write_coin_in_database
from currency.models import Currency

pytestmark = pytest.mark.django_db


class TestCurrencyUtils:
    
    def test_get_all_currency_data(self):
        data = get_all_currency_data()
        assert len(data) > 0

    def test_write_coin_in_database(self):
        data = get_all_currency_data()
        write_coin_in_database(data)
        assert Currency.objects.count() == 100
        
        assert Currency.objects.first().price != 0
        assert Currency.objects.first().market_cap != 0
