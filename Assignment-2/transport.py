# transport.py module

def get_bus_fare(distance_km):
    return distance_km * 0.5  # $0.5 per km

def get_train_fare(distance_km):
    rate = 0.75
    return distance_km * rate

def get_flight_fare(destination):
    fares = {'Pune': 5300, 'Mumbai': 3450, 'Mangalore': 7350}
    return fares.get(destination, 500) # Default fare if not found