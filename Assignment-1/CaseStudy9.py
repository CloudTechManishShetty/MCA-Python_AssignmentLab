balance = int(input("Please Enter Your Balance Amount that you want to credit: "))
print("=== Welcome to JSPM's ATM ===")

while True:
    print("\nYour Current Balance: ₹",balance)
    choice = input("Do you want to withdraw? (yes/no): ").lower()

    if choice == "no":
        print("Thank you for using our ATM. Goodbye!")
        break

    amount = int(input("Enter withdrawal amount: ₹"))

    if amount % 100 != 0:
        print("Error: Please enter amount in multiples of 100.")
        continue

    if amount > balance:
        print("Error: Insufficient balance.")
        continue

    balance -= amount
    print("Transaction Successful! You withdrew ₹",amount)
    print("Remaining Balance: ₹",balance)

    more = input("Do you want another transaction? (yes/no): ").lower()
    if more == "no":
        print("Thank you for using our ATM. Goodbye!")
        break
