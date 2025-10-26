class SeatsFullError(Exception):
    def __init__(self, flight_id):
        self.flight_id = flight_id
        super().__init__("Flight flight_id is fully booked. No seats available.")

MAX_SEATS = 2
BOOKED_SEATS = 0
LOG_FILE = "reservation_log.txt"

def book_ticket(flight_id, passenger_data):
    global BOOKED_SEATS
    file_resource = None
    
    print(f"\n--- Attempting to book for {flight_id} ---")
    
    try:
        if BOOKED_SEATS >= MAX_SEATS:
            raise SeatsFullError(flight_id)

        if not isinstance(passenger_data.get('name'), str) or len(passenger_data['name']) < 2:
            print("Booking failed: Invalid or missing passenger name.")
            return

        if not isinstance(passenger_data.get('age'), int) or passenger_data['age'] <= 0:
            print("Booking failed: Invalid passenger age.")
            return

        BOOKED_SEATS += 1
        
        file_resource = open(LOG_FILE, 'a')
        log_entry = f"BOOKED: Flight {flight_id}, Seat {BOOKED_SEATS}, Passenger: {passenger_data['name']}\n"
        file_resource.write(log_entry)
        
        print(f"Booking successful! Seat {BOOKED_SEATS} on {flight_id} for {passenger_data['name']}.")

    except SeatsFullError as e:
        print(f"Booking failed: {e}")
        
    except Exception as e:
        print(f"An unexpected error occurred during booking: {e}")

    finally:
        if file_resource:
            file_resource.close()
        print("--- Booking attempt finished. ---")
import os
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

# Test Case 1: Successful booking
book_ticket("AI101", {'name': 'Manish Shetty', 'age': 21})
# Test Case 2: Successful booking (max seats = 2)
book_ticket("AI101", {'name': 'Ganesh Katare', 'age': 22})
# Test Case 3: Seats full (Raises SeatsFullError)
book_ticket("AI101", {'name': 'Rohan Dubhale', 'age': 24})
# Test Case 4: Invalid passenger data (Handled gracefully with return)
book_ticket("AI102", {'name': '', 'age': 25}) 
# Test Case 5: Invalid passenger data (Handled gracefully with return)
book_ticket("AI102", {'name': 'Kaushal', 'age': 'twenty'}) 
print(f"\nTotal seats booked on AI101: {BOOKED_SEATS}/{MAX_SEATS}")
print(f"Check '{LOG_FILE}' for successful booking records.")