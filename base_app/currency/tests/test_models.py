''' test models '''
import pytest
import decimal
from django.db.models import Max
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from ..models import Currency


class TestCurrency:
    ''' testcase currency '''

    def test_create_currency(self):
        ''' test create currency '''
        mixer.blend('currency.Currency')
        assert Currency.objects.count() == 1

    def test_create_couple_currency(self):
        ''' test create coulpe currency '''
        mixer.cycle(5).blend('currency.Currency')
        assert Currency.objects.count() == 5

    def test_default_market_cap_is_zero(self):
        ''' test default market cap is zero '''
        currency = mixer.blend('currency.Currency')
        assert currency.market_cap == 0

    def test_default_price_currency_is_zero(self):
        ''' test default price is zero '''
        currency = mixer.blend('currency.Currency')
        assert currency.price == 0
