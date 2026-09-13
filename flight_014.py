#flight schedule organizer(using .sort(), .reverse(), .copy())
flights = ["EK212", "BA205", "QR45", "AA100", "DL88", "LH400", "AF678"]
print(f"{'=' * 6} FLIGHT SCHEDULE ORGANIZER {'=' * 6}")
print(flights)
flights_copy = flights.copy()#this creates a copy of the original list so that it is not affected by the sort() and reverse() methods
print(flights_copy)
flights.sort()#this sorts the list in ascending order
print(flights)
flights.reverse()# Sort in descending order
length_of_list = len(flights)#this calculates the length of the list
print(f"Total flights: {length_of_list}")
flights.sort(reverse=True)# Sort in descending order
print(flights)
print(flights_copy)#this demonstrates that the original list is not affected by the sort() and reverse() methods



#FLIGHT BOARD MANAGER (USING LIST METHODS)
flights = ["BA205", "QR45", "AA100", "EK212", "DL88", "LH400"]
print(f'{'=' * 6} FLIGHT BOARD MANAGER {'='  * 6}')
print(f'Original: {flights}')
flight_copy = flights.copy()#this creates a copy of the original
print(f'Backup copy: {flight_copy}')
flights.sort()#this sorts the list in ascending order
print(f'Using .sort(): {flights}')
flights.sorted()#this returns a sorted list without changing the original list
