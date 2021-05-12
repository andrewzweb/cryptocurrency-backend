import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from django.contrib.auth.models import User

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from dashboard.models import Dashboard
from dashboard.serializers import DashboardSerializer


class TestApiDashboard:
    '''testcase api dashboard'''
    
    def test_get_all_dashboard(self):
        '''test get all dashboard'''
        # TODO: make test
        pass

    def test_create_dashboard(self):
        ''' test create dashboard '''
        #TODO: make test
        pass
    
    def test_add_currency_to_dashboard(self):
        ''' test add currency to dashboard '''
        # TODO: make test
        pass
   
