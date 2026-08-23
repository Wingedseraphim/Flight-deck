#flight queue manager(list methods)
flight_queue = ["BA205", "QR45", "AA100", "EK212", "DL88"]
print(f'{'=' * 6} {'Flight queue manager'} {'=' * 6}')
print(f'Original queue: {flight_queue}')
flight_queue.append('LH400')
flight_queue.insert(2,'AF678')
flight_queue.extend(['KL901','SQ321'])
flight_queue.pop()
flight_queue.remove('AA100')
print(f'after append + insert + extend: {flight_queue}')
print(f'position of EK212: {flight_queue.index('EK212')}')
print(f'Number of BA205: {flight_queue.count('BA205')}')
print(f'Length now: {len(flight_queue)}')
flight_queue.clear()

#airplane seating matrix(2D indexing)
seats = [
    ["1A", "1B", "1C", "1D"],
    ["2A", "2B", "2C", "2D"],
    ["3A", "3B", "3C", "3D"],
    ["4A", "4B", "4C", "4D"]
]
print(seats[0])
print(seats[1])
print(seats[2])
print(seats[3])
seats[0][1] = "X"
seats[2][3] = "X"
print(seats[1][2])
length_of_seats = len(seats)
print(length_of_seats)
length_of_seats_per_row = len(seats[0])
print(length_of_seats_per_row)
seats[3] = ['x','x','x','x']
print(seats)

