import os
import inspect
from bitcoin_hypos.lib.config_reader import ConfigReader
from bitcoin_hypos.lib.config_types import ConfigTypes
from bitcoin_hypos.lib.spot_price import SpotPriceRetriever

#TODO: Reconsider whether the code in this class
# should go somewhere else or have a different name
class SituationBuilder():

  def __init__(self):
    self.config_reader = ConfigReader()

  def get_config_values(self):
    #TODO: use inspect modules to loop over all configs instead of just
    #inspecting one by one
    bitcoin = self.config_reader.all_config_values(ConfigTypes.Bitcoin)
    bitcoin_values = [round(float(amount),8) for amount in bitcoin.values()]
    debts = self.config_reader.all_config_values(ConfigTypes.Debts)
    debt_values = [round(float(amount),2) for amount in debts.values()]
    keep = self.config_reader.all_config_values(ConfigTypes.Keep)
    keep_value = next(round(float(amount),2) for amount in keep.values())
    return {'bitcoin': bitcoin_values, 'debts': debt_values, 'keep': keep_value}

