import argparse
from bitcoin_hypos.lib.spot_price import SpotPriceRetriever
from bitcoin_hypos.lib.calc_leftover import CashLeft
from bitcoin_hypos.lib.display_results import Results

def run():
  parser = argparse.ArgumentParser(description='Bitcoin Net Worth Calculator')
  parser.add_argument('btc', help='the amount of Bitcoin you own', nargs="+", type=float)
  parser.add_argument('debt', help='the amount of debt in USD that you would cover by potentially selling Bitcoin', nargs="+", type=float)
  parser.add_argument('--price', '-p', help='a price you set, instead of the default current spot price', type=float, nargs="?")
  parser.add_argument('--keep', '-k', help='the amount of Bitcoin you don\'t intend to sell to cover any debts', type=float, nargs="?", const=0.0, default=0.0)
  input_args = parser.parse_args()

  current_btc_price = SpotPriceRetriever().get_price()
  if input_args.price:
    current_btc_price = input_args.price
  cash_left = CashLeft(current_btc_price, input_args.btc, input_args.keep, input_args.debts).calc_leftover()
  Results.display_usd(cash_left)
