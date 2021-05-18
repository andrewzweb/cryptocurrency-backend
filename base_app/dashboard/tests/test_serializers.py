import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


from dashboard.serializers import DashboardSerializer


class TestDashboardSerializers:
    '''testcase serializers'''

    def test_dashboard_serializers(self):
        # TODO: write test for serializers
        pass
