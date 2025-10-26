current_balance = float(input("Enter your Current Account Balance (Rs.): "));
withdrawal_amount = float(input("Enter Withdrawal Amount (Rs.): "));

print("\n--- Processing Transaction ---");

if current_balance >= withdrawal_amount:
    new_balance = current_balance - withdrawal_amount;
        
    print("Transaction Successful!");
    print("Amount Withdrawn: Rs. ",withdrawal_amount);
    print("New Balance: Rs. ",new_balance);
        
else:
    print("Transaction Failed.");
    print("Insufficient Balance: Your current balance is too low for this withdrawal.");
    print("Current Balance: Rs. ",current_balance);
    print("Requested Withdrawal: Rs. ",withdrawal_amount);
print("----------------------------");