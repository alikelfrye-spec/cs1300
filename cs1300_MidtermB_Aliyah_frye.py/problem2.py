vehicle = input ("Vehicle type (car,motorcycle,truck):")
time = float(input ("How long where you parked?(# of hours) "))
parking_pass = input ("Do you have a parking pass?:(yes/no)")

if parking_pass == "yes":
    fee = "Free"
elif vehicle == "motorcycle":
    if time <= 2:
        fee = 1.00
    else:
        fee = 1.00 + ((time - 2) *.5)
elif vehicle == "car":
    if time <= 2:
        fee = 3.00
    else: 
        fee = 3.00 + ((time-2)*1.50)
elif vehicle == "truck":
    if time <= 2:
        fee = 5.00
    else: 
        fee = 5.00 + ((time-2)*2.50)
else:
    print ("Invalid vehicle type.")

print ("--- Parking recept ---")
print (f"vehicle:    {vehicle}")
print (f"Duration:   {time}")
print (f"Pass holder:{parking_pass}")
print (f"Fee:        ${fee}")
print ("-" * 22)