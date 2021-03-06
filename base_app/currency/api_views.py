from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Currency
from .serializers import *


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def currency_list(request):
    """
    List  currency, or create a new currency.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        currencies = Currency.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(currencies, 20)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CurrencySerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/currency/?page=' + str(nextPage), 'prevlink': '/api/currency/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def currency_detail(request, pk):
    """
    Retrieve, update or delete a currency by id/pk.
    """
    try:
        currency = Currency.objects.get(pk=pk)
    except Currency.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CurrencySerializer(currency,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CurrencySerializer(currency, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        currency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
