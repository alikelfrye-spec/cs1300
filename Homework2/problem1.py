name = input("Print first and last name:")
age = int(input("How old are you?:"))
hobby = input("What is your favorite hobby?")

decorative_border = "=" * 30
width = 30

print(f"{decorative_border}")
print(f"USER PROFILE CARD".center(width))
print(f"{decorative_border}")
print(f"Name:     {name}")
print(f"Age:      {age}")
print(f"Hobby:    {hobby}")
print(f"{decorative_border}")
print(f"Thank you for creating your profile!".center(width))
print(f"{decorative_border}")
