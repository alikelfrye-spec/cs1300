errors =[]
valid_majors = ["CS", "IT", "CE", "DS"]
student_id = input("Enter student id:")
name = input("Enter full name:")
age_input = input("Enter your age:")
major = input ("Enter your major:")

if not student_id.strip():
   errors.append( "Student id can't be empty. ")
elif len(student_id) != 8: 
    errors.append(f"Student id must be 8 digits got {len(student_id)}.")
elif not student_id[0].isalpha():
    errors.append("Student id must start with a letter .")
else:
    student_id_verify=(f"Student Id:{student_id}")
    
if not name.strip():
    errors.append("Name cant be empty.")
elif len(name)<= 2:
    errors.append(f"Name must be at least 2 letters. got {len(name)}.")

else:
    name_verify=(f"Student Name:{name}")
    
try:
    age = int(age_input)
    if not 16<= age <= 99:
        errors.append("Age must be between 16 and 99.")
    else:
        age_verify=(f"Student Age:{age}")
except ValueError:
    errors.append("Age must be a number.")  
    
if  major.upper() not in ["CS", "IT", "CE", "DS"]:
    errors.append ("majors must be CS, IT, CE,or DS.")
else:
    major_verify= (f"Student Major: {major}")

if not errors:
     print ("Profile created succesfully")
     print (student_id_verify)
     print (name_verify)
     print (age_verify)
else:
    print ("Please fix the following errors.")
    for error in errors:
     print(f"-{error}")

    

    
    

