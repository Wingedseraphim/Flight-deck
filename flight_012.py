#airplane seating chart (2d matrix)
seats = [
    ["1A", "1B", "1C", "1D"],
    ["2A", "2B", "2C", "2D"],
    ["3A", "3B", "3C", "3D"],
    ["4A", "4B", "4C", "4D"]
]
print(f'{'=' * 6} {'AIRPLANE SEATING CHART'} {'=' * 6}')
print(seats)
print(f'Seat 2C: {seats[1][2]}')
print(f'Seat 4C: {seats[3][2]}')
print(f'Row 3: {seats[3]}')
print('After Booking:')
seats[0][1] = 'X'
seats[2][3] = 'X'
seats[3][2] = 'X'
print(seats)
print(f'window seats: \t{seats[0][0]} {seats[0][3]}\n\t\t{seats[1][0]} {seats[1][3]}\n\t\t{seats[2][0]} {seats[2][3]}\n\t\t{seats[3][0]} {seats[3][3]}')
seats[0] = ['X','X','X','X']
print(seats[0])
second_flight_seats = [
    ['1A', '1B']
    ['2A', '2B']
    ['3A', '3B']
]