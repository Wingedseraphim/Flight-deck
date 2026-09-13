#S3RAPHIM Aircraft status dictionary
# This dictionary contains the status of various aircraft in the S3RAPHIM system.
aircraft_status = [{
    "registration": "N12345",
    "aircraft_type": "Boeing 737",
    "altitude": 35000,
    "airspeed": 450,
    "fuel_remaining": 5000,
    "engine_temperature": 600,
    "status": "Cruise",
    "heading": "270",
    "vertical_speed": 0
},
{
    "registration": "N67890",
    "aircraft_type": "Airbus A320",
    "altitude": 30000,
    "airspeed": 400,
    "fuel_remaining": 4500,
    "engine_temperature": 550,
    "status": "Descent",
    "heading": "090",
    "vertical_speed": -500
},
{
    "registration": "N54321",
    "aircraft_type": "Boeing 747",
    "altitude": 38000,
    "airspeed": 500,
    "fuel_remaining": 6000,
    "engine_temperature": 650,
    "status": "Cruise",
    "heading": "180",
    "vertical_speed": 0
},
{
    "registration": "N98765",
    "aircraft_type": "Airbus A380",
    "altitude": 40000,
    "airspeed": 550,
    "fuel_remaining": 7000,
    "engine_temperature": 700,
    "status": "Cruise",
    "heading": "270",
    "vertical_speed": 0
}]
print("=" * 6, "S3RAPHIM AIRCRAFT STATUS", "=" * 6)
print(f'Full dictionary: {aircraft_status}')# this prints the entire list of dictionaries containing the aircraft status information
print(f'Registration: {aircraft_status[0]["registration"]}')#this prints the value associated with the "registration" key in the first dictionary of the aircraft_status list
print(f'Altitude: {aircraft_status[0]["altitude"]}')#this prints the value associated with the "altitude" key in the first dictionary of the aircraft_status list
print(f'Current status: {aircraft_status[0]["status"]}')#this prints the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'After update: Status is now: {aircraft_status[0]["status"]}')# this updates the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'Heading: {aircraft_status[0]["heading"]}')#this prints the value associated with the "heading" key in the first dictionary of the aircraft_status list
print(f'Vertical Speed: {aircraft_status[0]["vertical_speed"]}')#this prints the value associated with the "vertical_speed" key in the first dictionary of the aircraft_status list
print(f'Fuel Remaining: {aircraft_status[0]["fuel_remaining"]}')#this prints the value associated with the "fuel_remaining" key in the first dictionary of the aircraft_status list
print(aircraft_status[0].pop("vertical_speed", None))#this deletes the vertical_speed key-value pair from the dictionary

print(f'Registration: {aircraft_status[1]["registration"]}')#this prints the value associated with the "registration" key in the first dictionary of the aircraft_status list
print(f'Altitude: {aircraft_status[1]["altitude"]}')#this prints the value associated with the "altitude" key in the first dictionary of the aircraft_status list
print(f'Current status: {aircraft_status[1]["status"]}')#this prints the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'After update: Status is now: {aircraft_status[1]["status"]}')# this updates the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'Heading: {aircraft_status[1]["heading"]}')#this prints the value associated with the "heading" key in the first dictionary of the aircraft_status list
print(f'Vertical Speed: {aircraft_status[1]["vertical_speed"]}')#this prints the value associated with the "vertical_speed" key in the first dictionary of the aircraft_status list
print(f'Fuel Remaining: {aircraft_status[1]["fuel_remaining"]}')#this prints the value associated with the "fuel_remaining" key in the first dictionary of the aircraft_status list
print(aircraft_status[1].get("status", "Descending"))# Print the value associated with the "status" key using the get() method, and if the key does not exist, return "Descending"
print(aircraft_status[1].get("heading", "80N40SW"))# here, 80N40SW can be assinged to a value and that variable should have the formula for calculating the heading of the aircraft
print(aircraft_status[1].get("vertical_speed", "0"))# here, 0 can be assinged to a value and that variable should have the formula for calculating the vertical speed of the aircraft
print("fuel_remaining" in aircraft_status[1])# this checks if the key "fuel_remaining" exists in the second dictionary of the aircraft_status list
print(aircraft_status[1].pop("heading", None))#this deletes the heading key-value pair from the dictionary

print(f'Registration: {aircraft_status[2]["registration"]}')#this prints the value associated with the "registration" key in the first dictionary of the aircraft_status list
print(f'Altitude: {aircraft_status[2]["altitude"]}')#this prints the value associated with the "altitude" key in the first dictionary of the aircraft_status list
print(f'Current status: {aircraft_status[2]["status"]}')#this prints the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'After update: Status is now: {aircraft_status[2]["status"]}')# this updates the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'Heading: {aircraft_status[2]["heading"]}')#this prints the value associated with the "heading" key in the first dictionary of the aircraft_status list
print(f'Vertical Speed: {aircraft_status[2]["vertical_speed"]}')#this prints the value associated with the "vertical_speed" key in the first dictionary of the aircraft_status list
print(f'Fuel Remaining: {aircraft_status[2]["fuel_remaining"]}')#this prints the value associated with the "fuel_remaining" key in the first dictionary of the aircraft_status list 
print(aircraft_status[2].get("status", "Descending"))# Print the value associated with the "status" key using the get() method, and if the key does not exist, return "Descending"
print(aircraft_status[2].get("heading", "80N40SW"))# here, 80N40SW can be assinged to a value and that variable should have the formula for calculating the heading of the aircraft
print(aircraft_status[2].get("vertical_speed", "0"))# here, 0 can be assinged to a value and that variable should have the formula for calculating the vertical speed of the aircraft
print("fuel_remaining" in aircraft_status[2])# this checks if the key "fuel_remaining" exists in the third dictionary of the aircraft_status list
print(aircraft_status[2].pop("status", None))#this deletes the vertical_speed key-value pair from the dictionary

print(f'Registration: {aircraft_status[3]["registration"]}')#this prints the value associated with the "registration" key in the first dictionary of the aircraft_status list
print(f'Altitude: {aircraft_status[3]["altitude"]}')#this prints the value associated with the "altitude" key in the first dictionary of the aircraft_status list
print(f'Current status: {aircraft_status[3]["status"]}')#this prints the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'After update: Status is now: {aircraft_status[3]["status"]}')# this updates the value associated with the "status" key in the first dictionary of the aircraft_status list
print(f'Heading: {aircraft_status[3]["heading"]}')#this prints the value associated with the "heading" key in the first dictionary of the aircraft_status list
print(f'Vertical Speed: {aircraft_status[3]["vertical_speed"]}')#this prints the value associated with the "vertical_speed" key in the first dictionary of the aircraft_status list
print(f'Fuel Remaining: {aircraft_status[3]["fuel_remaining"]}')#this prints the value associated with the "fuel_remaining" key in the first dictionary of the aircraft_status list
print(aircraft_status[3].get("status", "Descending"))# Print the value associated with the "status" key using the get() method, and if the key does not exist, return "Descending"
print(aircraft_status[3].get("heading", "80N40SW"))# here, 80N40SW can be assinged to a value and that variable should have the formula for calculating the heading of the aircraft
print(aircraft_status[3].get("vertical_speed", "0"))# here, 0 can be assinged to a value and that variable should have the formula for calculating the vertical speed of the aircraft
print("fuel_remaining" in aircraft_status[3])# this checks if the key "fuel_remaining" exists in the fourth dictionary of the aircraft_status list
print(aircraft_status[3 ].pop("engine_temperature", None))#this deletes the engine_temperature key-value pair from the dictionary




