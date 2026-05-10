sentence = input("Enter a sentence:")
upper_count = 0
lower_count = 0
number_count = 0
space_count = 0

for char in sentence: 
    if char.isupper(): 
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit:
        number_count += 1
    elif char.isspace():
        space_count += 1
    
print (f"Uppercase letters:{upper_count}")
print (f"Lowercase letters:{lower_count}")
print (f"Numbers:          {number_count}")
print (f"Number of spaces: {space_count} ")
print (f"Reversed:          {sentence[::-1]}")