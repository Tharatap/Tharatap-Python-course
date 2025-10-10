"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone_number = input("Enter phone number: ")


# name validation
nameFlag = True
ageFlag = True 
phoneFlag = True
for i in name:
    if i.isalpha() == False and i == " ":
        nameFlag = True
        
    elif i.isalpha() == False:
        nameFlag = False
        break


if 18>age>65:
    ageFlag = False


if len(phone_number) != 10:
    phoneFlag = False
else:
    for i in phone_number:
        if i.isdigit() == False:
            phoneFlag = False
            break
print("\nValidation Results: ")
if nameFlag:
    print(f"Valid (contains only letters and spaces)")
else:
    print("Name: Invalid")
if ageFlag:
    print(f"Valid ({age} years old)")
else:
    print("Age: Invalid")
if phoneFlag:
    print("Valid (10-digit number)\n")
else:
    print("phone number: Invalid\n")

print("Formatted Information: ")
print(f"Name: {name.upper()}")
if 18<=age<=30:
    print("Age Group: Young Adult (18-30)")
else: 
    print("Age Group: Noy Young Adult")
print(f"Phone: +66-{phone_number[1:]}")
        
