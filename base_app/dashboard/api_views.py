
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from currency.models import Currency
from account.models import Account

from dashboard.serializers import DashboardSerializer
from account.serializers import AccountSerializer
from currency.serializers import CurrencySerializer

#@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET', 'POST'])
def dashboard_list(request):
    """
    List  dashboard, or create a new currency.
    """
    
    if request.method == 'GET':
        account = Account.objects.first()
        currencies = Currency.objects.all()
        data = {
            'account': AccountSerializer(account).data,
            'currency': [CurrencySerializer(currencies, many=True).data]
        }
        print('data', data)
        serializer = DashboardSerializer(data, many=True)
        print(serializer.data)
        return Response({'data': serializer.data})

#    elif request.method == 'POST':
#        serializer = DashboardSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
