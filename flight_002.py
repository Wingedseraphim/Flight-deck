#FUEL CALCULATOR
# This program calculates the amount of fuel needed for a flight based on distance and fuel efficiency.
fuel_loaded = float(input("Enter total fuel loaded (L): "))
fuel_burned_per_hr = float(input("Enter the fuel burned per hour (L): "))
current_fuel = float(input("Current fuel available (L): "))
fuel_capacity = float(input("Enter current fuel capacity (L): "))
estimated_endurance = fuel_loaded / fuel_burned_per_hr
fuel_percentage = (current_fuel / fuel_capacity) * 100
#FLIGHT TIME
#This program calculates the estimated flight time based on distance and speed.
distance = float(input("Enter the distance to be traveled (km): "))
speed = float(input("Enter the cruising speed (km/h): "))
flight_time = distance / speed
#ALTITUDE
#This program calculates the estimated altitude based on the flight plan.
current_altitude = float(input("Enter current altitude (ft): "))
climb_rate = float(input("Enter climb rate (ft/min): "))
time_climbing = float(input("Enter time climbing (min): "))
new_altitude = current_altitude + (climb_rate * time_climbing)
#DISTANCE
#This program calculates the distance traveled based on speed and time.
total_distance = float(input("Enter total distance traveled (km): "))
distance_traveled = float(input("Enter distance traveled (km): "))
remaining_distance = total_distance - distance_traveled
#AIRSPEED
#This program calculates the airspeed based on distance and time.
ground_speed = float(input("Enter ground speed (km/h): "))
headwind = float(input("Enter headwind (km/h): "))
true_speed = ground_speed - headwind
#BATTERY LEVEL (FOR DRONES)
#this program calculates the estimated battery percentage based on current charge and battery capacity.
current_charge = float(input("Enter current battery charge (%): "))
battery_capacity = float(input("Enter battery capacity (mAh): "))
battery_percentage = (current_charge / battery_capacity) * 100
#ENGINE TEMPERATURE
#this program calculates the estimated engine temperature based on current temperature and time.
outside_temperature = float(input("Enter outside temperature (°C): "))
temperature_rise = float(input("Enter temperature rise per hour (°C): "))
engine_temperature = outside_temperature + temperature_rise
print("=" * 57)
print("           S3RAPHIM FLIGHT DATA   ")
print(f"*Estimated flight endurance        : {estimated_endurance:.2f} hours")
print(f"*Estimated flight time             : {flight_time:.2f} hours")
print(f"*Estimated new altitude            : {new_altitude} ft")
print(f"*Fuel Remaining                    : {fuel_percentage:.2f} %")
print(f"*Remaining distance to destination : {remaining_distance:.2f} km")
print(f"*Estimated true airspeed           : {true_speed} km/h")
print(f"*Estimated battery percentage      : {battery_percentage:.2f} %")
print(f"*Estimated engine temperature      : {engine_temperature} °C")
print("*Flight Status                     : READY")
print("=" * 57)