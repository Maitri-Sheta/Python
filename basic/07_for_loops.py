#through string
name=input("Enter your name:")
for char in name:
    print(char)

#through list
size = int (input("Enter the size of the list:"))
fruit=[]
for i in range(size):
    a=input("Enter fruits name:")
    fruit.append(a)


#using break statement
for f in fruit:
    print(f)
    if f=="banana":
        print("found banana")
        break

print("\n")
#using continue statement
for f in fruit:
    print(f)
    if f=="maitri":
        continue


#range statement and else statement
t=int(input("Want table of ??:"))
for i in range(1,11):
    print(t," * " ,i," = ",t*i)
else:
    print("Table of ",t," is completed")

print("\n")
#patterns
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#patterns
print("\n")
n=int(input("Enter a number of rows:"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
