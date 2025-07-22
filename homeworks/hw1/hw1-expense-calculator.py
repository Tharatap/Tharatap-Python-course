"""
Personal Finance Calculator
Student: [Your Name]
Date: [Today's Date]
Purpose: Calculate monthly budget and savings
"""
Monthly_income = float(input("monthly income in THB: "))
rent_cost = float(input("Monthly rent/housing cost: "))
food_budget = int(input("Monthly food budget in THB:  "))
transportation_cost = float(input("Monthly transportation expenses: "))
entertainment_budget = int(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency: "))
# กันผู้ใช้กรอกเกิน 100 % 
while emergency_fund_percent > 100:
    print("Please fill in the information again")
    emergency_fund_percent = float(input("Percentage to save for emergency: "))
investment_percent = float(input("Percentage to inves: "))
# กันผู้ใช้กรอกเกิน 100 % 
while investment_percent > 100:
    print("Please fill in the information again")
    investment_percent = float(input("Percentage to inves: "))

#calculate
Total_Fixed_Expenses = rent_cost + transportation_cost
Total_Variable_Expenses = food_budget + entertainment_budget
Total_Expenses = Total_Fixed_Expenses + Total_Variable_Expenses
Remaining_Income = Monthly_income - Total_Expenses
Emergency_Fund_Amount = Monthly_income * (emergency_fund_percent / 100)
Investment_Amount = Monthly_income * (investment_percent / 100)
Available_for_Savings = Remaining_Income - Emergency_Fund_Amount - Investment_Amount
Expense_Ratio = (Total_Expenses / Monthly_income) * 100

#output
print("=== MONTHLY BUDGET REPORT ===")
print("Income: ",Monthly_income," THB")
print("Fixed Expenses: ",Total_Fixed_Expenses," THB")
print("Variable Expenses: ",Total_Variable_Expenses," THB")
print("Total Expenses: ",Total_Expenses," THB")
print("Remaining: ",Remaining_Income,"THB")
print("\n")
print("=== SAVINGS BREAKDOWN===")
print(f"Emergency Fund ({emergency_fund_percent}): {Emergency_Fund_Amount} THB")
print(f"Investment({investment_percent}): {Investment_Amount} THB")
print(f"Available for Savings: {Available_for_Savings}")
print("\n")
print(f"Expense Ratio: {Expense_Ratio}%")
