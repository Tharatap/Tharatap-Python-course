"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

weight = float(input("How much do you weigh?(KG.): "))
height = float(input("How tall are you?(M.): "))
BMI = (weight / (height ** 2))
print(f"Your BMI = {BMI:.1f}")
if BMI > 30:
    print(f"BMI Categories: Obese")
elif 25.0<=BMI<=29.9:
    print(f"BMI Categories: Overweight ")
elif 18.5 <= BMI <= 24.9:
    print(f"BMI Categories: Normal weight")
else:
    print(f"BMI Categories: Underweight")