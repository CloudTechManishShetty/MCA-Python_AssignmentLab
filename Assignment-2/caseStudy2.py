def summarize_orders(orders):
    print("--- E-commerce Order Summary ---")
    
    if not orders:
        print("No orders to summarize.")
        return

    total_orders = len(orders)
    print("Total number of orders: ",total_orders)

    highest_order = max(orders)
    lowest_order = min(orders)
    print("Highest order value: ",highest_order)
    print("Lowest order value: ",lowest_order)

    total_value = sum(orders)
    average_order = total_value / total_orders
    print("Average order value: ",average_order)

    sorted_orders = sorted(orders)
    print("\nOrders sorted (ascending):")
    value = [values for values in sorted_orders]
    print(value)
    
    print("-" * 32)

order_values = [150.75, 89.99, 245.50, 42.10, 150.75, 12.00, 305.00, 78.45]

summarize_orders(order_values)