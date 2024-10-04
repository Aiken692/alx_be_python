import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance with an initial balance of 100 for this example
    account = BankAccount(100)

    # Ensure that a command is provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and the optional amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Execute based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use 'deposit', 'withdraw', or 'display'.")

if __name__ == "__main__":
    main()
