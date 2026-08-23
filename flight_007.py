#FLIGHT STATUS CHECKER (STRING METHODS)
raw_message = "  flIgHt ba205 to lOnDoN heAthRoW is dElAyEd due to weAtHeR. gate b12.  "
raw_message_02 = raw_message.upper()
print(raw_message_02)
raw_message_01 = raw_message.lower()
print(raw_message_01)
print(raw_message_01.capitalize())
print(raw_message_01.find("delayed"))
print(raw_message_01.find("gate"))
print(raw_message.replace("dElAyEd", "DELAYED"))
print(raw_message.replace("lOnDoN heAthRoW", "London Heathrow"))
raw_message_03 = bool("weather" in raw_message or "weather" in raw_message_01 or "weather" in raw_message_02)
print(raw_message_03)
if raw_message_01.find("weather") != True:
        print("Weather condition found in the message.")
elif raw_message_01.find("weather") == False:
            print("No weather information")