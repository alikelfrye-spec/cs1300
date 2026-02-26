a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
c = int(input("Enter value for c:"))

# this is asking for the user imput.

if a < b < c :
    print("a < b < c          :True")
else:
    print("a < b < c         :False")
    
if not (a > b or b > c ):
    print("not a > b or b > c :True")
else:
    print("not a > b or b > c:False")

if a <= b and b <=c :
    print("a <= b and b <=c   :True")
else:
    print("a <= b and b <=c  :False")
    
    #this is saying if its true print true if not print false
    
if not (a > b or b > c) is (a <= b and b <=c):
    print ("De Morgans confirmed : Expressions 2 and 3 match")
else:
    print("De Morgans not confirmed : Expressions 2 and 3 don't match")
    
    
    #this part is evaluating expressions 2 and 3 and determining if both match and if they aren't it prints false.