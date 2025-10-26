# --- Decorator to check authentication ---
def authenticate_user(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            print("❌ Access denied. Please log in first.")
            return
        return func(user, *args, **kwargs)
    return wrapper


# --- Generator function for last 5 transactions ---
def transaction_history(transactions):
    # Yield last 5 transactions
    for txn in transactions[-5:]:
        yield txn


# --- Function to perform a transaction (uses decorator) ---
@authenticate_user
def perform_transaction(user, amount):
    print(f"✅ Transaction of ₹{amount} successful for user: {user['name']}")


# --- Example usage ---
if __name__ == "__main__":
    # User data
    user = {"name": "Manish", "is_logged_in": False}

    # Sample transaction list
    transactions = [500, -200, 1000, -150, 300, -400, 700]

    # Perform a transaction
    perform_transaction(user, 250)

    # Display last 5 transactions using generator
    print("\nLast 5 Transactions:")
    for txn in transaction_history(transactions):
        print(f"₹{txn}")
