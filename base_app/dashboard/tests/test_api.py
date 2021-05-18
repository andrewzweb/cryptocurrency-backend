import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
import json
from rest_framework.test import APITestCase, RequestsClient, APIClient
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from dashboard.models import Dashboard
from dashboard.serializers import DashboardSerializer
from currency.models import Currency
from account.models import Account


class TestApiDashboard(APITestCase):
    '''testcase api dashboard'''

    def setUp(self):
        '''setup'''
        
        self.client = APIClient()

        # gen user data
        self.user_data = {
            'username':'UserName',
            'email':'user@email.com',
            'password':'UserPassword'
        }

        # create user
        self.user = User.objects.create_user(**self.user_data)
        assert User.objects.count() == 1

        # create account
        self.account = Account.objects.create(user=self.user, name='UserName')
        assert Account.objects.count() == 1

        #create currency
        mixer.cycle(5).blend('currency.Currency')
        assert Currency.objects.count() == 5
        
    def test_get_url_dashboard(self):
        ''' test get currency '''

        url = reverse('api_dashboard_list')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_get_all_dashboard(self):
        '''test get all dashboard'''

        mixer.cycle(5).blend('dashboard.Dashboard')
        assert Dashboard.objects.count() == 5

        url = reverse('api_dashboard_list')
        response = self.client.get(url, format='json')

        data = DashboardSerializer(Dashboard.objects.all(), many=True).data
        assert data == response.data['data']
        
    def test_create_dashboard(self):
        ''' test create dashboard '''

        # login before send date
        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password']
        )

        data = {
            "pk": 1,
            "account": {},
            "currency": []
        }
        
        url = reverse('api_dashboard_list')
        response = self.client.post(url, data, format='json')
        print(response.content)
        print(response.data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Dashboard.objects.count() == 1
        
    def test_add_currency_to_dashboard(self):
        ''' test add currency to dashboard '''

        dashboard = Dashboard.objects.create(account=self.account)

        currency = Currency.objects.create(
            name='Alt',
            symbol='alt',
            price='10.40',
            market_cap=110
        )

        # login before send date
        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password']
        )
        
        data = {
            "pk": 1,
            "account": {},
            "currency": [
                {
                    "pk": currency.id,
                    "name": currency.name,
                    "symbol": currency.symbol,
                    "market_cap": currency.market_cap,
                    "price": currency.price
                }
            ]
        }

        url = reverse('api_dashboard_detail', kwargs={'pk': dashboard.id})
        response = self.client.put(url, data, format='json')

        dashboard_from_db = Dashboard.objects.get(pk=dashboard.pk)
        assert dashboard_from_db.currency.all()[0] == currency
