#AVIATION FLIGHT INFORMATION DISPLAY
#using fstrings \n \t 

airport_name = input("Enter the name of the airport: ")
flight_number = input("Enter your flight number: ")
destination_city = input("Enter your destination city: ")
aircraft_type = input("Enter the type of aircraft: ")
departure_time = input("Enter the departure time (HH:MM): ")
gate_number = input("Enter the gate number: ")
status = input("Enter the flight status: ")
print (f"{'*' * 5} {airport_name} {'*' * 5}\nFlight Information\n{"-" * 60}\nFlight: \t{flight_number}\nDestination: \t{destination_city}\nAircraft: \t{aircraft_type}\nDeparture: \t{departure_time}\nGate: \t\t{gate_number}\nStatus: \t{status}\nHave a nice and safe flight!\n{"-" * 60}")