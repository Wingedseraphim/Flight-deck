#Flight deck access code masker.
pilot_username = input("Enter your pilot username: ")
access_code = input("Enter your access code: ")
masked_code = '*' * len(access_code)
print(f'{"=" * 5} {"FLIGHT DECK ACCESS"} {"=" * 5}')
print(f'Pilot: {pilot_username.upper()}')
print(f'Access Code: {masked_code}')
print(f'Length: {len(access_code)} characters')
if len(access_code) < 3:
    print("Warning: Access code is too short. It should be at least 8 characters long.")
else:
    print('Strong access code.')