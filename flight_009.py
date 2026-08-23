#PILOT EXPERIENCE CALCULATOR
print(f"{"=" * 5} {"PILOT EXPERIENCE CALCULATOR"} {"=" * 5}")
pilot_name = input("What is your name? ")
flying_hours = int(input("What year did you get your pilot license? "))
experience = 2026 - flying_hours
print(f'Pilot Name: {pilot_name}')
print(f'Licence Year: {flying_hours}')
print(f'Years of Experience: {experience}')
print(f'Status: {"Experienced Pilot" if experience >= 5 else "Novice"}')
if experience < 0:
    print('warning: You entered a future year. Please enter a valid year.')
else:
    print(f"You have {experience} years of flying experience.")