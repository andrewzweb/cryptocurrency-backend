''' Test Account'''

import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse

from .. import views
from .. import models


@pytest.mark.django_db
class TestViewAccount:

    def setup(self):
        self.user = User.objects.create_user(
            'UserName',
            'user@email.com',
            'UserPassword'
        )
        self.account = models.Account.objects.create(
            user=self.user,
            name='UserName'
        )
        self.client = Client()

    def test_login_page_exist(self):
        response = self.client.get(
            reverse('account:login'))
        assert 'sing in' in str(response.content)

    def test_login_user(self):
        response = self.client.post(
            reverse('account:login'),
            {
                'username': 'UserName',
                'password': 'UserPassword'
            }
        )
        assert response.status_code == 302
