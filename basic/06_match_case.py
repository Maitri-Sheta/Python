#match with constants
a=int(input("Enter a number between 1 and 5: "))
match a:
    case 1:
        print("Enterd 1")
    case 2:
        print("Enterd 2")
    case 3:
        print("Enterd 3")
    case 4:
        print("Enterd 4")
    case 5:
        print("Enterd 5")
    case _:
        print("Invalid input")


#match with OR statement
match a:
    case 1|3|5:
        print("Odd number")
    case 2|4:
        print("Even number")
    case _:
        print("Invalid input")


#match with if condition
match a:
    case a if a<3:
        print("Less than 3")
    case a if a==3:
        print("Equal to 3")
    case a if a>3:
        print("Greater than 3")
    case _:
        print("Invalid input")


#match with list
size=int(input("Enter the size of list:"))
lst=[]
for i in range(size):
    d=int(input("Enter the element:"))
    lst.append(d)

match lst:
    case []:
        print("Empty list")
    case [x]:
        print("Single element list:",x)
    case [x,y]:
        print("Two element list:",x,y)
    case [x,y,*rest]:
        print("List with more than two elements. First two elements are:",x,y)
    case _:
        print("Invalid input")

