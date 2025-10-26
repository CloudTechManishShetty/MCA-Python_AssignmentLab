import transport as t
from stay import calculate_hotel_cost, calculate_food_expense

print("Enter your Travel and stay Details: ")
dest = input("Enter Destination Name: ")
distance = int(input("Enter the Total Distance from your Current Location to destination in km: "))
mode = input("Enter the mode of your transport: ")
nights = int(input("Enter Total no of nights you will stay: "))
days = int(input("Enter Total no of Days you will stay: "))

travel_cost = 0

if mode == "flight":
    travel_cost = t.get_flight_fare(dest)
elif mode == "bus":
    travel_cost = t.get_bus_fare(distance)
elif mode == "train":
    travel_cost = t.get_train_fare(distance)
else:
    print("Enter Correct mode of Transport!")

hotel_cost = calculate_hotel_cost(nights)
food_cost = calculate_food_expense(days)

total_trip_cost = travel_cost + hotel_cost + food_cost

# --- Display Results ---
print("Travel Cost to ",dest," : ",travel_cost)
print("Hotel Cost for ",nights," nights: ",hotel_cost)
print("Food Cost for ",days," days: ",food_cost)
print("-" * 30)
print("Total Trip Cost: ",total_trip_cost)