string = "15"
number = 7
print("Explicit Typecasting")
print("Type of a",type(string))
print("Type of b",type(number))
str_num = int(string) #throws an error if the string is not a valid integer
sum = number + str_num
print ("The sum of",number,"and",string,"is:",sum)
print("Type of sum:",type(sum))


print("\nImplicit Typecasting")
num1=5.6
print("Type of a:",type(num1))
num2=4
print("Type of b:",type(num2))
sum=num1+num2
print("The sum of",num1,"and",num2,"is:",sum)
print("Type of sum:",type(sum))