
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from currency.models import Currency
from account.models import Account
from dashboard.models import Dashboard

from dashboard.serializers import DashboardSerializer
from account.serializers import UserSerializer
from currency.serializers import CurrencySerializer
from django.contrib.auth.models import User



#@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET', 'POST'])
def dashboard_list(request):
    """
    List  dashboard, or create a new dashboard.
    """
    
    if request.method == 'GET':
        '''get all dashboard '''
        serializer = DashboardSerializer(Dashboard.objects.all(), many=True, read_only=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        '''create new dashboard'''
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
