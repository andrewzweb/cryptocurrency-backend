''' Test views '''

import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from .. import views

class TestCurrencyList:
    ''' test currency list view '''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory()

    def test_get_currency_list_view(self):
        ''' test get home view '''
        resp = views.currency_list(self.req)
        assert resp.status_code == 200
