from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from currency.models import Currency
from django.conf import settings 


def get_all_currency_data():

    data = []

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'100',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': settings.API_KEY_FOR_COINMARKET,
    }

    session = Session()
    session.headers.update(headers)
    
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return data

def write_coin_in_database(data):

    result = False
    
    if len(data) > 0:
        for coin in data:
            try: 
                item = Currency.objects.get(name=coin['name'])
                item.market_cap = int(coin['quote']['USD']['market_cap'])
                #item['price'] = int(coin['quote']['USD']['price'])
                item.save()
            except:
                Currency.objects.create(
                    name=coin['name'],
                    symbol=coin['name'],
                    market_cap=coin['quote']['USD']['market_cap'],
                    price=coin['quote']['USD']['price'],
                )
        result = True
                
    return result
