''' test models '''

import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
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

    def test_create_account(self):
        ''' test create account '''

        account = Account.objects.create(
            user=self.user,
            name='Test'
        )

        assert Account.objects.count() == 1

    def test_can_not_create_user_without_django_user(self):
        ''' can not create user without django user '''

        with pytest.raises(ObjectDoesNotExist):
            account = Account.objects.create(
                name='Test'
            )
        assert Account.objects.count() == 0
