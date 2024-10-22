# person = {'name': 'Alice', 'age': 25}
# print(person['age'])
# person['age'] = 50
# print(person['age'])

# importing the module
import pywhatkit
import datetime
# using Exception Handling to avoid unprecedented errors
CurrentTime = datetime.datetime.now()
print(CurrentTime)
hour = CurrentTime.hour
min = CurrentTime.minute +1
try:
# sending message to receiver using pywhatkit
    pywhatkit.sendwhatmsg("+27780398251""+27797738156""+27697568202""+27680674602""+2768563112","lunch Time!!!!!!!!!!!", 11,59)
    print("Successfully Sent!")
except:
# handling exception and printing error message
    print("An Unexpected Error!")