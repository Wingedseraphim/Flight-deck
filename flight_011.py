#Flight List slicer
flights = ["BA205", "QR45", "AA100", "EK212", "DL88", "LH400", "AF678", "KL901", "SQ321", "CX889"]
print(f'{"=" * 5} {"FLIGHT LIST SLICER"} {"=" * 5}')
print(f'1. First 4 flights: \t\t{flights[0:4]}')
print(f'2. First 3 flights: \t\t{flights[0:3]}')
print(f'3. From index 5 onwards: \t{flights[5:]}')
print(f'4. Last 3 flights: \t\t{flights[-3:]}')
print(f'5. Reversed list: \t\t{flights[::-1]}')
print(f'6. Every 2nd flight: \t\t{flights[::2]}')

#MUTABLE AIRCRAFT STATUS BOARD(USING INDEXING)
aircraft_status = ["On Time", "Delayed", "On Time", "Boarding", "Cancelled", "On Time"]
print('aircraft_status before change:', aircraft_status)
aircraft_status[1] = "Now Boarding"
aircraft_status[4] = "Diverted"
aircraft_status[-1] = "Departed"
print('aircraft_status after change:', aircraft_status)
aircraft_status[0:2] = ["Gate Closed", "Final Call"]
print('aircraft_status after slice change:', aircraft_status)