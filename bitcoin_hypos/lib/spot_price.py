from bitcoin_hypos.lib.config_reader import ConfigReader
from bitcoin_hypos.lib.config_types import ConfigTypes
from coinbase.wallet.client import Client
import requests

class SpotPriceRetriever():

  def __init__(self):
    config_reader = ConfigReader()
    key = config_reader.value(ConfigTypes.Coinbase, 'api_key')
    secret = config_reader.value(ConfigTypes.Coinbase, 'api_secret')
    self.client = Client(key, secret)

  def get_price(self):
    try:
      spot_price = self.client.get_spot_price(current_pair = 'BTC-USD')
    except requests.HttpError as exception:
      print(exception)
    return round(float(spot_price['amount']),8)
