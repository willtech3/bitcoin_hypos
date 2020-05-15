import argparse
from bitcoin_hypos.lib.situation_builder import SituationBuilder
from bitcoin_hypos.lib.spot_price import SpotPriceRetriever
from bitcoin_hypos.lib.calc_leftover import CashLeft
from bitcoin_hypos.lib.display_results import Results

def run():
  parser = argparse.ArgumentParser(description='Bitcoin Net Worth Calculator')
  parser.add_argument('--price', '-p', help='a price you set, instead of the default current spot price', type=float, nargs="?")
  input_args = parser.parse_args()
  sb = SituationBuilder()
  values = sb.get_config_values()
  current_btc_price = SpotPriceRetriever().get_price()
  if input_args.price:
    current_btc_price = input_args.price
  cash_left = CashLeft(current_btc_price, values['bitcoin'], values['keep'], values['debts']).calc_leftover()
  Results.display_usd(cash_left)


