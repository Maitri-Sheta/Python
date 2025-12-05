import time
timestamp = time.strftime("%H:%M:%S")
print("Current time: ",timestamp)

if (timestamp < "12:00:00") :
    print("Good Morning")
elif (timestamp == "12:00:00"):
    print("Good Noon")
elif (timestamp >"12:00:00" and timestamp < "18:00:00"):
    print("Good Afternoon")
else:
    print("Good Evening")