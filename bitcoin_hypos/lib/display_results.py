from termcolor import colored

class Results(object):

  @staticmethod
  def display_usd(amount):
    amount = round(amount, 2)
    display_amount = '$' + str(amount)
    if amount < 0:
      print()
      print(f"You would owe {colored(display_amount, 'red')}")
      print()
    else:
      print()
      print(f"You would have {colored(display_amount, 'green')}")
      print()


