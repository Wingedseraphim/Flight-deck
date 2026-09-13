#flight record
# this program creates a flight record using a dictionary and demonstrates how to access and update its values. It also shows how to handle missing keys using the get() method and how to create a list of flight records.

flight = {
    "callsign": "S3raphom3829",
    "aircraft": "private_jet",
    "altitude": 5000.876,
    "speed": 600.7,
    "heading": 6078.789,
    "status": "in_transit",
}



print(f'Callsign: {flight.get("callsign")}')
print(f'Aircraft: {flight["aircraft"]}')
print(f'Altitude: {flight.get("altitude")}')
print(f'Speed: {flight["speed"]}')
print(f'Heading: {flight.get("heading")}')
print(f'Status: {flight["status"]}')

flight.update({"altitude": 6000.123})
flight.update({"speed": 700.456})
flight.update({"heading": 7000.789})
flight.update({"status": "landed"})
flight.update({"aircraft": "commercial_airliner"})
flight.update({"callsign": "S3raphim007"})
print(flight["altitude"])
print(flight["speed"])
print(flight["heading"])
print(flight["status"])
print(flight["aircraft"])
print(flight["callsign"])

flight_destination = flight.get("destination", "LHR")  # Print the value associated with the "destination" key using the get() method, and if the key does not exist, return "LHR"
print(flight_destination)
flight_duration = flight.get("duration", "4 hours")  # Print the value associated with the "duration" key using the get() method, and if the key does not exist, return "4 hours"
print(flight_duration)
flight_tracking = flight.get("tracking", "enabled")  # Print the value associated with the "tracking" key using the get() method, and if the key does not exist, return "enabled"
print(flight_tracking)



flight_1 = {
    "callsign": "S3raphom3829",
    "aircraft": "private_jet",
    "altitude": 5000.876,
    "speed": 600.7,
    "heading": 6078.789,
    "status": "in_transit",
}
flight_2 = {
    "callsign": "S3raphom3829",
    "aircraft": "private_jet",
    "altitude": 5000.876,
    "speed": 600.7,
    "heading": 6078.789,
    "status": "in_transit",
}
flight_3 = {
    "callsign": "S3raphom3829",
    "aircraft": "private_jet",
    "altitude": 5000.876,
    "speed": 600.7,
    "heading": 6078.789,
    "status": "in_transit",
}
flights = [
    flight_1, 
    flight_2, 
    flight_3
    ]
print(flights)