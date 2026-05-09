Age = int(input("Enter Your Age:"))
if Age < 0:
    print ("Age cannot be negative.")
else:
    Showing_input = input ("Is this a matinee showing? (yes/no):") 
    Showing = True if Showing_input == "yes" else False


if Age >= 65:
    if Showing == True:
        ticket_price = 6.00
else:
    ticket_price = 7.00
    
if Age >= 18:
    if  Showing == True:
        ticket_price = 7.00
else:
    ticket_price = 13.00
    
if Age >= 17:
    if Showing == True:
       ticket_price = 7.00
else: 
    ticket_price = 10.00
    
if Age > 13:
    if Showing == True:
        ticket_price = 6.00
else:
    ticket_price = 8.00
    
print(f"Your ticket price is: ${ticket_price:.2f}")