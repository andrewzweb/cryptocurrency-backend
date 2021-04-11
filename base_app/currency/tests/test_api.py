import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Currency
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from ..serializers import CurrencySerializer


class TestApiCurrency(APITestCase):

    def setup(self):
        self.client = RequestsClient()

    @pytest.mark.skip
    def test_get_currencies_list(self):
        ''' test get currency list '''

        mixer.cycle(5).blend('currency.Currency')
        assert Currency.objects.count() == 5
        url = reverse('api_currency_list')
        response = self.client.get(url, format='json')
        assert response.status_code, status.HTTP_200_OK

        data_from_db = CurrencySerializer(Currency.objects.all())

        assert data_from_db in response.data

    def test_add_currency(self):
        ''' test create currency '''

        url = reverse('api_currency_list')
        data = {
            'name': 'NewCurrency',
            'symbol': 'NC',
            'market_cap': '1000',
            'price': '1'
        }

        response = self.client.post(url, data, format='json')
        assert response.status_code, status.HTTP_201_CREATED
        assert Currency.objects.count() == 1
        assert Currency.objects.first().name == 'NewCurrency'

    def test_get_currency(self):
        ''' test get currency '''

        obj = mixer.blend('currency.Currency')
        assert Currency.objects.count() == 1
        url = reverse('api_currency_detail', kwargs={'pk': obj.id})
        response = self.client.get(url, format='json')
        assert response.status_code, status.HTTP_200_OK
