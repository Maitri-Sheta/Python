name = input("Enter your name: ")
country = input("Enter your country: ")

typicaly ="My name is {} and i'm from {}."
print(typicaly.format(name, country))


typicaly ="My name is {0} and i'm from {1}."
print(typicaly.format(name, country))

latest =f"My name is {name} and i'm from {country}."
print(latest)

latest =f"My name is {{name}} and i'm from {{country}}."
print(latest)

raw_string = r"C:\Users\Name\Documents\file.txt"
print(raw_string)

multi_line = """This is a multi-line string.
It can span multiple lines.
Useful for long texts."""
print(multi_line)

