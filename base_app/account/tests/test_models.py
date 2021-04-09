''' test models '''

import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from ..models import Account


@pytest.mark.django_db
class TestAccount:
    ''' testcase account '''

    def setup(self):
        self.user = User.objects.create_user(
            'Andrew',
            'my@email.com',
            'secret_pass')

    def test_create_account(sefl):
        ''' test create account '''

        account = Account.objects.create(
            user=self.user,
            name='Test'
        )

        assert Account.objects.count() == 1
        assert account.name ==  Account.objects.first().name
