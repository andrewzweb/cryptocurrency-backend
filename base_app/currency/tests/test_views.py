''' Test views '''

import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
from .. import views
pytestmark = pytest.mark.django_db


class TestCurrencyList:
    ''' test currency list view '''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory()

    def test_get_currency_list_view(self):
        ''' test get home view '''
        resp = views.currency_list(self.req)
        assert resp.status_code == 200

    def test_view_show_currency_data(self):
        ''' test view show currency data '''
        currencies = mixer.cycle(5).blend('currency.Currency')
        resp = views.currency_list(self.req)

        for currency in currencies:
            assert currency.name in str(resp.content)
            assert currency.symbol in str(resp.content)
            assert str(currency.price) in str(resp.content)
            assert str(currency.market_cap) in str(resp.content)
