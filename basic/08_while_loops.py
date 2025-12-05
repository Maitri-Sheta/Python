n=int(input("Enter a number: "))
#break statement
i=1
while i<=10:
    print(n, " * ",i," = ",n*i)
    i+=1
    if i==n:
        break

#continue statement
print("\n")
i=1
while i<=10:
    print(n, " * ",i," = ",n*i)
    i+=1
    if i==n:
        continue

#else statment
print("\n")
i=0
while i<7:
    print(i)
    i+=1
else:
    print("loop is ended")