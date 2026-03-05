weight= float( input("Enter weight here:"))
unit_system = input("Enter unit system (M/I):")



if unit_system == "I":
    height= float(input("Enter Height (inches):"))
    bmi = (weight*703) / (height ** 2)
  
elif unit_system == "M":
    height= float(input("Enter Height (meters):"))
    bmi= weight / (height ** 2) 
else:
    print ("Invalid unit system.")
if bmi >= 30:
    category = "Obese"
elif bmi >= 25:
    category = "Overweight"
elif bmi >= 18.5:
    category = "Normal weight"
else:
    category = "Under weight"
        
print (f"BMI:      {bmi:.1f}")
print (f"Category: {category} ")
       

