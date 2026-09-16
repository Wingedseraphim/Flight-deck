#AIRCRAFT TRACKING SETS
morning = ["BA123", "EK202", "BA123", "LH400", "QR10"]
afternoon = ["EK202", "LH400", "AF999", "QR10", "QR10"]
evening = ["BA123", "AF999", "LH400", "BA123"]

unique_morning_flights = set(morning)
print(unique_morning_flights)
unique_afternoon_flights = set(afternoon)
unique_evening_flights = set(evening)
unique_flights = unique_afternoon_flights.intersection(unique_evening_flights)
print(unique_morning_flights.intersection(unique_flights))
print(unique_morning_flights.intersection(unique_afternoon_flights))
print(unique_morning_flights.difference(unique_afternoon_flights))
print(unique_morning_flights.isdisjoint(unique_afternoon_flights))
aircrafts = unique_morning_flights.union(unique_afternoon_flights)
total_aircrafts = aircrafts.union(unique_evening_flights)
print(total_aircrafts)
print(unique_evening_flights.issubset(total_aircrafts))
morning_copy = unique_morning_flights.copy()
morning_copy.clear()
print(morning_copy)
print(unique_morning_flights)
morning_copy.add("AF999")
morning_copy.add( "LH400")
morning_copy.add("BA123")
print("BA123" in morning_copy)
print(list(total_aircrafts))

# easier way to add unique values in a given example
t = unique_morning_flights.union(unique_afternoon_flights).union(unique_evening_flights)
print(t)