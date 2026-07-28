#FLIGHT RECORD EXTRACTOR (STRING INDEXING AND SLICING)
flight_record = "BA205-LHR-2245-B787-0NTIME-GATEB12"
print(f"{"=" * 5} {"FLIGHT RECORD EXTRACTED"} {"=" * 5}\nAirline: \t{flight_record[0:2]}\nFlight No: \t{flight_record[2:5]}\nDestination: \t{flight_record[6:9]}\nDeparture: \t{flight_record[10:13]}\nAircraft: \t{flight_record[15:19]}\nStatus: \t{flight_record[20:26]}\nGate: \t\t{flight_record[27:]}")
print(f"Callsign: \t{flight_record[0:5]}")
destination = flight_record[6:9]
print(destination[::-1])
print(flight_record[::2])