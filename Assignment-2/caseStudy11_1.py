def process_payment():
    print("--- Online Payment Processing ---")
    
    try:
        amount_str = input("Enter payment amount (e.g., 50.00): ")
        
        amount = float(amount_str)
        
        if amount <= 0:
            print("Payment failed: Amount must be positive.")
        else:
            print("Payment of ",amount," processed successfully.")

    except ValueError:
        print("Payment failed: Invalid amount entered.")
        print("Please enter a valid numeric value (e.g., 50.00).")
    except Exception as e:
        print("An unexpected error occurred: ",e)

process_payment()