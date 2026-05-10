temp = float(input("Enter the current tempature:"))
scale = input ("Enter the scale (C/F):")

if scale.upper() == "C":
    temp_scale = (temp-32)*5/9 
    print (f"{temp:.1f}°C = {temp_scale:.1f}°F")
elif scale.upper() == "F":
    temp_scale = temp * 9/5 + 32
    print (f"{temp:.1f}°F = {temp_scale:.1f}°C")
else:
    print ("Invalid scale")
    

