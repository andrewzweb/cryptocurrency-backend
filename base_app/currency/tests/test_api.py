import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from django.contrib.auth.models import User

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from ..models import Currency
from ..serializers import CurrencySerializer

import json


class TestApiCurrency(APITestCase):
    '''test case api currency'''
    
    def setup(self):
        self.client = RequestsClient()

    def test_get_currency(self):
        ''' test get currency '''

        obj = mixer.blend('currency.Currency')
        assert Currency.objects.count() == 1
        url = reverse('api_currency_detail', kwargs={'pk': obj.id})
        response = self.client.get(url, format='json')
        assert response.status_code, status.HTTP_200_OK

    def test_get_list_without_login(self):
        '''test get list without login'''

        # create 5 items
        mixer.cycle(5).blend('currency.Currency')
        assert Currency.objects.count() == 5

        # get list
        url = reverse('api_currency_list')
        request = self.client.get(url)
        assert request.status_code == 200

        # make serializer
        currency = Currency.objects.all()
        serializer = CurrencySerializer(currency, many=True)

        # what in data base we get in response 
        assert serializer.data == request.data['data']
        
    def test_create_currency_with_login(self):
        '''test create currency with login'''

        # create user
        self.user_data = {
            'username':'UserName',
            'email':'user@email.com',
            'password':'UserPassword'
        }
        User.objects.create_user(**self.user_data)

        # login before send date
        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password']
        )

        # send data
        url = reverse('api_currency_list')
        data = {
            'id': 10,
            'name': 'ArcCoin',
            'symbol': 'ARC',
            'price': 10,
            'market_cap': 100
        }
        request = self.client.post(url, json.dumps(data), content_type='application/json')

        # check
        assert request.status_code == 201
        assert Currency.objects.count() == 1

    def test_create_currency_without_login(self):
        '''test create currency with login'''

        # send data
        url = reverse('api_currency_list')
        data = {
            'id': 10,
            'name': 'ArcCoin',
            'symbol': 'ARC',
            'price': 10,
            'market_cap': 100
        }
        request = self.client.post(url, json.dumps(data), content_type='application/json')

        # check
        assert request.status_code == 403
        assert Currency.objects.count() == 0
