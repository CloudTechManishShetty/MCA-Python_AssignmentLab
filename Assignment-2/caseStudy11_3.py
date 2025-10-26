class InsufficientFundsError(Exception):
    def __init__(self, requested, balance):
        self.requested = requested
        self.balance = balance
        super().__init__("Withdrawal amount (",requested,") exceeds available balance (",balance,").")

class NotMultipleOfHundredError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__("Withdrawal amount (",amount,") must be a multiple of 100.")

def atm_withdrawal(current_balance):
    print("\n--- ATM Withdrawal Simulation ---")
    print("Current Balance: ",current_balance)

    try:
        amount_str = input("Enter withdrawal amount (multiple of 100): $")
        
        withdrawal_amount = int(amount_str) 

        if withdrawal_amount % 100 != 0:
            raise NotMultipleOfHundredError(withdrawal_amount)

        if withdrawal_amount > current_balance:
            raise InsufficientFundsError(withdrawal_amount, current_balance)
        
        new_balance = current_balance - withdrawal_amount
        print("Transaction successful! Withdrew ",withdrawal_amount)
        print("New Balance: ",new_balance)

    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")
    
    except NotMultipleOfHundredError as e:
        print("Error",e)

    except InsufficientFundsError as e:
        print("Transaction failed: ",e)
        print("Please enter a lower amount.")

    except Exception as e:
        print(f"An unexpected system error occurred: {e}")

atm_withdrawal(current_balance=2500) # Valid transaction
atm_withdrawal(current_balance=2500) # Test InsufficientFundsError (e.g., enter 3000)
atm_withdrawal(current_balance=2500) # Test NotMultipleOfHundredError (e.g., enter 250)
atm_withdrawal(current_balance=2500) # Test ValueError (e.g., enter 'five hundred')