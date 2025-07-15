"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""


Chose = input("THB to USD (Select 1) or USD to THB (Select 2): ")
money = float(input("How much to Converter: "))
if Chose == '1':
    money = money / 35.5 #thai to USD
    print(f"Currency can be converted = {money:.2f} USD")
elif Chose == '2':
    money = money * 35.5 # USD to thai
    print(f"Currency can be converted = {money:.2f} Bath")
else:
    print("Error number Please Select Converter again ")
