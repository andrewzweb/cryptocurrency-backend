from base_app.settings.celery import app
import time
import random
from .utils import get_all_currency_data, write_coin_in_database


@app.task(bind=True)
def update_database(self):

    # get data all coin from app
    all_coin = get_all_currency_data()
    print(all_coin)
    # put on data in database
    write_coin_in_database(all_coin)
    return all_coin
