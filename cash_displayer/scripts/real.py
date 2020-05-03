from cash_displayer.lib.situation_builder import SituationBuilder
from cash_displayer.lib.spot_price import SpotPriceRetriever
from cash_displayer.lib.calc_leftover import CashLeft
from cash_displayer.lib.display_results import Results

def run():
  sb = SituationBuilder()
  values = sb.get_config_values()

  current_btc_price = SpotPriceRetriever().get_price()
  cash_left = CashLeft(current_btc_price, values['bitcoin'], values['keep'], values['debts']).calc_leftover()
  Results.display_usd(cash_left)


