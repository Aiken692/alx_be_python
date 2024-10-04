class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a new bank account with an optional initial balance (default is 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient balance is available.
        Returns True if withdrawal is successful, otherwise False.
        """
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
