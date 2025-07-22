# Complete this program to classify people by age
#age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter age: "))
if  0 <= age <= 12:
    print(f"age = {age}:  Your are Child") 
elif 13 <= age <=19:
    print(f"age = {age}:  Your are Teenager")
elif 20 <= age <=59:
    print(f"age = {age}:  Your are adult")
else:
    print(f"age = {age}:  Your are Senior")