# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 # each topping, any size
# ----- Order Storage -----
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99
decorative_border = "="*30
print ("Welcome to the pizza shop!")

while True:
    print (decorative_border)
    print ("         PIZZA SIZES")
    for i in range(len(sizes)):
        print (f"{i+1} {sizes[i]:<20}${size_prices[i]:> 5.2f}")
    print (decorative_border)
    
    while True:
        try:
            choice = input("Pick a size 1-4:") 
            size_index = int(choice) -1
            if 0 <= size_index < len(sizes):
                base_price = size_prices[size_index]
                selected_size_name = sizes [size_index]
                break
            else: 
                print ("Invalid size choice.")
        except ValueError:
            print ("Please pick a number.")
        
    selected_toppings = []
    print ("Toppings cost $1.50 each.")
    for i in range(len(topping_names)):
        print (f"{i+1} {topping_names[i]}" )
    while True:
        topping_input = input("Pick topping # or done:").lower()
        if topping_input == "done":
            break
        try:
            topping_index = int (topping_input) -1
            if 0 <= topping_index < len(topping_names):
                topping_name = topping_names[topping_index]
                if topping_name in selected_toppings:
                    print (f"Already added {topping_name}")
                    continue
                else:
                    selected_toppings.append(topping_name)
                    print (F"{topping_name} Added!")
            else:
                print(f"Please enter 1-{len(topping_names)} or done.")
        except ValueError:
            print ("Invalid input please pick a number or done.")
    pizza_price = base_price + (len(selected_toppings)* topping_price)
    
    if not selected_toppings:
        desc = F"{selected_size_name} Cheese"
    else:
        desc = f"{selected_size_name} " + ", ".join(selected_toppings)
        
    order_descriptions.append(desc)
    order_prices.append(pizza_price)
    
    while True:
        again = input ("Would you like to order another?(Yes/No):").lower()
        if again in ["yes", "no"]:
            break
        print ("Please enter yes or no.")
        
    if again == "no":
            break
    
if not order_descriptions:
        print ("No Pizzas ordered. See you next time!")
        
else:
    discount = 0.0
    attempts = 0
    while attempts < 3: 
        code = input ("Enter discount code or 'none':").upper()
        if code == "NONE":
            break
        elif code == "STUDENT10":
            discount = 0.10
            print ("10 percent discount applied.")
        elif code == "HALFOFF":
            discount = 0.50
        print ("50 percent discount applied.")
        break
    else:
        attempts += 1
        print (f"Invalid code {3 - attempts} remaining.")

if attempts == 3:
    print ("no discount applied")

print (decorative_border)
print ("      YOUR ORDER RECIPT ")
print (decorative_border)

subtotal = 0
for i in range (len(order_descriptions)):
    print (f"{i+1} {order_descriptions[i]}")
    print(f"   ${order_prices[i]:>6.2f}")
    subtotal += order_prices[i]

discount_amount = subtotal * discount 
tax = (subtotal - discount_amount) * 0.07
final_total = (subtotal - discount_amount) + tax

print (decorative_border)
print(f"Subtotal:   ${subtotal:>6.2f}")
if discount_amount > 0:
    print (f"Discout:   ${discount_amount:>6.2f}")
print (f"Tax:   ${tax:>6.2f}")
print (decorative_border)

most_expensive = max(order_prices)
print (f"Most expensive pizza:  ${most_expensive:>6.2f}")

print ("Order by size:")
for size in sizes:
    count = 0
    for desc in order_descriptions:
        if size in desc:
            count +=1
    print (f"{size}:{count}")
    
print ("Thank you for your order. We hope to see you back soon!")
    