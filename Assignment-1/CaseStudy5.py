units_consumed = int(input("Enter total units consumed: "));

if units_consumed <= 100:
    bill = units_consumed * 5;
elif units_consumed <= 300:
    bill = (100 * 5) + (units_consumed - 100) * 7;
else:
    bill = (100 * 5) + (200 * 7) + (units_consumed - 300) * 10;

print("Total Electricity Bill = ₹", bill);
 