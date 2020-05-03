
class CashLeft:

  def __init__(self, spot_price, amounts, keep, debts):
    self.keep = keep
    self.spot_price = spot_price
    self.amounts = amounts
    self.debts = debts

  def calc_leftover(self):
    total_btc = sum(self.amounts) - self.keep
    total_debt = sum(self.debts)
    return round(float(self.spot_price * total_btc - total_debt),2)

