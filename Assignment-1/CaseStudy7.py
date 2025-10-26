products = [("Apple", 50), ("Banana", 0), ("Milk", 30), ("Orange", 20), ("Bread", 25)];

total = 0;
for item, price in products:
    if price == 0 and item != "Exit":
        print("Skipping ",item," (Price is 0)");
        continue;
        
    if item == "Exit":
        print("Exit found! Stopping cart scan...");
        break;        
    pass;

    print("Adding ",item," - ₹",price);
    total += price;
else:
    print("All products scanned successfully!");

    print("Total Bill Amount = ₹", total);