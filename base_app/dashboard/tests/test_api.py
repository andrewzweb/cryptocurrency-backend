import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

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
            'account': {},
            'dashboard':[]
        }
        
        url = reverse('api_dashboard_list')
        response = self.client.post(url, data,  format='json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Dashboard.objects.count() == 1
        
    def test_add_currency_to_dashboard(self):
        ''' test add currency to dashboard '''
        # TODO: make test
        pass
   

