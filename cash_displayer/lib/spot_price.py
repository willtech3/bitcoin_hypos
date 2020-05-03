from cash_displayer.lib.config_reader import ConfigReader
from cash_displayer.lib.config_types import ConfigTypes
from coinbase.wallet.client import Client

class SpotPriceRetriever():

  def __init__(self):
    config_reader = ConfigReader()
    key = config_reader.value(ConfigTypes.Coinbase, 'api_key')
    secret = config_reader.value(ConfigTypes.Coinbase, 'api_secret')
    self.client = Client(key, secret)

  def get_price(self):
    spot_price =  self.client.get_spot_price(current_pair = 'BTC-USD')
    return round(float(spot_price['amount']),8)
