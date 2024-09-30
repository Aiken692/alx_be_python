class BankAccount:
  def __init__(self, initial_balance=0.0):
    self.balance = initial_balance

  def deposit(self, amount):
    """Deposits the specified amount into the account."""
    self.balance += amount
    print(f"Deposited: ${amount}")

  def withdraw(self, amount):
    """Withdraws the specified amount from the account, returning True if successful."""
    if amount > self.balance:
      print("Insufficient funds.")
      return False
    else:
      self.balance -= amount
      print(f"Withdrew: ${amount}")
      return True

  def display_balance(self):
    """Prints the current account balance."""
    print(f"Current Balance: ${self.balance}")