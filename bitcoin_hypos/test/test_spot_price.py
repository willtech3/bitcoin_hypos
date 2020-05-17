import pytest
import requests
import requests_mock
import json
from requests import HTTPError
from bitcoin_hypos.lib.config_reader import ConfigReader
from bitcoin_hypos.lib.config_types import ConfigTypes
from bitcoin_hypos.lib.spot_price import SpotPriceRetriever
from coinbase.wallet.client import Client

class TestSpotPrice:

  @pytest.fixture
  def requests_mock(self, request):
    m = requests_mock.Mocker()
    m.start()
    request.addfinalizer(m.stop)
    return m

  def test_get_price(self, requests_mock):
    # set up the fake API response because we
    # don't want out code tests to make API calls all the time
    mock_response = {
     "data": {
       "amount": "1015.00",
       "currency": "USD"
     }
    }
    uri = f"{Client.BASE_API_URI}v2/prices/BTC-USD/spot"
    requests_mock.get(uri, json=mock_response)

    # execute code under test
    spr = SpotPriceRetriever()
    current_btc_price = spr.get_price()

    # assert the results
    assert type(current_btc_price) is float
    assert current_btc_price == 1015.00



