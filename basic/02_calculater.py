
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nArithmetic Operations ")
print("Adddition:", num1+num2)
print("Subtraction:", num1-num2)
print("Multiplication:",num1*num2)
print("Dvision:",num1/num2)
print("Floor Division:",num1//num2)
print("Exponetiation:",num1**num2)
print("Modulus:",num1%num2)


print("\nComparison Operations ")
print("Equal to:", num1==num2)      
print("Not Equal to:", num1!=num2)
print("Greater than:", num1>num2)
print("Less than:", num1<num2)
print("Greater than or Equal to:", num1>=num2)
print("Less than or Equal to:", num1<=num2)

print("\nLogical Operations ")
print("Logical AND:", (num1>0) and (num2>0))
print("Logical OR:", (num1>0) or (num2>0))
print("Logical NOT:", not(num1>0))

print("\nBitwise Operations ")
print("Bitwise AND:", int(num1) & int(num2))
print("Bitwise OR:", int(num1) | int(num2))
print("Bitwise XOR:", int(num1) ^ int(num2))
print("Bitwise NOT:", ~int(num1))
print("Bitwise Left Shift:", int(num1) << 2)
print("Bitwise Right Shift:", int(num1) >> 2)

print("\nAssignment Operations ")
a = num1
a += num2
print("a += num2:", a)     
a = num1
a -= num2
print("a -= num2:", a)
a = num1
a *= num2       
print("a *= num2:", a)
a = num1
a /= num2   
print("a /= num2:", a)
a = num1
a %= num2
print("a %= num2:", a)
a = num1
a **= num2
print("a **= num2:", a)
a = num1
a //= num2
print("a //= num2:", a)

print("\nMembership Operations ")
list_numbers = [num1, num2, 10, 20, 30]
print("num1 in list_numbers:", num1 in list_numbers)
print("num2 not in list_numbers:", num2 not in list_numbers)

print("\nIdentity Operations ")
b = num1
print("num1 is b:", num1 is b)
print("num1 is not num2:", num1 is not num2)

