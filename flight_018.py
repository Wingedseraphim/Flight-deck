#flight position tracker

flights = [
    {
    "callsign": "S3RAPHIM01",
    "position": (6.5244, 3.3792),
    "altitude": 60000
},
{
    "callsign": "S3RAPHIM02",
    "position": (7.5244, 4.3792),
    "altitude": 35000
},
{
    "callsign": "S3RAPHIM03",
    "position": (8.5244, 5.3792),
    "altitude": 47283
}
]
print(flights)

print(f'Callsign: {flights[0]["callsign"]}')
print(f'Callsign: {flights[1]["callsign"]}')
print(f'Callsign: {flights[2]["callsign"]}')

print(f'Position: {flights[0]["position"]}')
print(f'Position: {flights[1]["position"]}')
print(f'Position: {flights[2]["position"]}')

print(f'Altitude: {flights[0]["altitude"]}')
print(f'Altitude: {flights[1]["altitude"]}')
print(f'Altitude: {flights[2]["altitude"]}')

if flights[0]["altitude"] > 30000:
    print(f'Flight {flights[0]["callsign"]} is above 30,000 feet.')
if flights[1]["altitude"] > 30000:
    print(f'Flight {flights[1]["callsign"]} is above 30,000 feet.')
if flights[2]["altitude"] > 30000:
    print(f'Flight {flights[2]["callsign"]} is above 30,000 feet.')

position = (6.5244, 3.3792)
print(position[0])  # prints the latitude
print(position[1])  # prints the longitude

flights_backup = flights[2].copy()
flights[2].update({"altitude": 70000})
print(flights[2]["altitude"])

print(flights[2])
print(flights_backup)