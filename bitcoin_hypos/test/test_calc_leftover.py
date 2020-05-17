import pytest
from bitcoin_hypos.lib.calc_leftover import CashLeft


class TestCashLeftover:

  @pytest.fixture
  def fake_data(self):
    bitcoin_values = [1.00000000, 0.1, 0.5, 0.01]
    debts = [1000, 10000.0, 2500]
    keep = 0.1
    return {'bitcoin': bitcoin_values, 'debts': debts, 'keep': keep, 'price': 10000.00 }

  def test_leftover_calculation(self, fake_data):
    cash_left = CashLeft(fake_data['price'], fake_data['bitcoin'], fake_data['keep'], fake_data['debts']).calc_leftover()
    assert sum(fake_data['bitcoin']) == 1.61
    assert sum(fake_data['debts']) == 13500.00
    assert cash_left == (10000.0 * (1.61 - 0.1)) - 13500.00


  def test_bad_values(self, fake_data):
    fake_data['bitcoin'] = [-17]
    cl = CashLeft(fake_data['price'], fake_data['bitcoin'], fake_data['keep'], fake_data['debts'])
    #assert cl.calc_leftover() raise BitcoinHypoErrors.NegativeBitcoinException
    pass
