import sys
from bank_account import BankAccount

def main():
    # Initialize a bank account with an initial balance of $100 for testing
    account = BankAccount(100)

    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and amount from the arguments
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform the appropriate action based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
