#In an e-commerce website, 
# we need to calculate discounts, 
# apply coupon codes, add taxes, and generate the final bill.
#  Instead of writing this logic again and again,
#  we use a function called generateInvoice()
#  that takes product price, tax rate, 
# and discount as inputs and returns the final amount.”

def generateInvoice(product_price, tax_rate, discount):
   tax = product_price * tax_rate
   discount_amut = product_price * discount
   final_price = product_price + tax - discount_amut
   return final_price

print("Final Bill: " , generateInvoice(2000,0.18,0.10))

#function without arguments
def welcome_message():
   print("Welcome to our E-commerce Website!")
welcome_message()

#function with arguments 
def greeting(name="Guest"):
   print("Hello, "+name+" !Welcome")
greeting()
greeting("Maitri")

#function with keyword arbitrary arguments
def name(**name):
   print("Hello, ",name['first']," ",name['last']," !Welcome")
name(last="Sheta",first="Maitri")