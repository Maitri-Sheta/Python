#basic
a=input("Enter a number:")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{a} * {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Program ended successfully.")


"""syntax error : parsing error
    interpreter stop the execution

    Exception : during execution error occur
    built in exception:
    SyntaxError
    TypeError
    ValueError
    IndexError
    KeyError
    ZeroDivisionError
    FileNotFoundError
    ImportError
    IOError
    KeyboardInterrupt
    ImportError
    EOFError
"""

#raise Exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        return "Minor"
    else:
        return "Adult"
try:
    user_age = int(input("Enter your age: "))
    status = check_age(user_age)
    print(f"You are an {status}.")
except Exception as e:
    print(f"An error occurred: {e}")
print("Program ended successfully.")

