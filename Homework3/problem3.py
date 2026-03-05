name = input ("Enter students name:")
exam1 = float (input ("Enter exam 1 score:"))
exam2 = float (input ("Enter exam 2 score:"))
exam3 = float (input ("Enter exam 3 score:"))

average = (exam1 + exam2 + exam3) / 3

if average >= 90:
    Grade = "A"
elif average >= 87:
    Grade = "A-"
elif average >= 83:
    Grade = "B+"
elif average >= 80:
    Grade = "B"
elif average >= 77:
    Grade = "B-"
elif average >= 73:
    Grade = "C+"
elif average >= 70:
    Grade = "C"
elif average >= 67:
    Grade = "C-"
elif average >= 63:
    Grade = "D+"
elif average >= 60:
    Grade = "D"
else:
    Grade = "F"

if average >= 90:
    standing = "Dean's List"
elif average >= 70:
    standing = "Good Standing"
elif average >= 60:
    standing = "Academic Probation"
else:
    standing = "Acedmic Suspesion Warning"
    
print ("\n"+ "="*30)
print ("   Grade report")
print (f"Student:      {Name}")
print (f"Exam1:       {exam1}")
print (f"Exam2:       {exam2}")
print (f"Exam3:       {exam3}")
print ("\n"+ "="*30)
print (f"Average:   {average}")
print (f"letter grade:{Grade}")
print (f"Status :  {standing}")
print ("\n"+ "="*30)
    