#flight record manager
#
flight = {
    "callsign": "S3RAPHIM01",
    "aircraft": "B737",
    "altitude": 35000,
    "speed": 450,
    "heading": 270,
    "status": "normal"
}
print(flight.get("callsign","unknown"))
print(flight.get("destination", "not found"))
print(flight.get("altitude", "unknown"))

print(flight.keys())
print(flight.values())
print(flight.items())

print("altitude" in flight)
print("fuel" in flight)
print(flight.get("fuel", "not found"))
new_data_1 = flight.update({"destination": "india"})
new_data_2 = flight.update({"fuel": 67892})
new_data_3 = flight.update({"pilot name": "s3raphim"})
print(flight)
backup = flight.copy()
flight.update({"altitude": 50000})
flight.update({"speed": 6789})
print(flight)
print(backup)
deleted_data = flight.pop("fuel")
print(deleted_data)


    
#Destructive iterations
flights = {
    "S3RAPHIM01": {"origin": "JFK", "destination": "LAX", "status": "on time"},
    "S3RAPHIM02": {"origin": "LHR", "destination": "CDG", "status": "delayed"},
    "S3RAPHIM03": {"origin": "SFO", "destination": "NRT", "status": "boarding"}
}

#unfnished code, need to learn loops and iterations to complete this section
