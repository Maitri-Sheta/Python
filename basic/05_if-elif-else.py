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

''' short hand if_else
syntex
    true_statment if condition else else_statement
used when the condition being tested is simple and execution of code is short.
'''
#short_hand if_else
a,b=25,36
print("A") if a>b else ("=") if a==b else print("B")
#typically way
if (a>b):
    print("A")
else:
    if (a==b):
        print("=")
    else:
        print("B")
