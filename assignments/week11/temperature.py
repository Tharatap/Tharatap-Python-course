"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
#รับค่า
def get_temperatures():
    daily_tem = []
    # รับข้อมูล จาก user ว่า
    for i in range(0,7):
        tem = float(input(f"Enter temperature day[{i+1}]: "))
        daily_tem.append(tem)
    return daily_tem
# คำนวณโจทย์
def analyze_temps(temp_list):
    avg = sum(temp_list) / len(temp_list)
    high_temp = max(temp_list)
    lowest_temp = min(temp_list)
    return (avg,high_temp,lowest_temp)
#show output
def display_analysis(avg,high,low):
    print(f"Temperature Analysis for the Week: ")
    print(f"Average: {avg:.2f} c")
    print(f"Highest: {high:.2f} c")
    print(f"Lowest: {low:.2f} c")
avg,high,low = analyze_temps(get_temperatures()) # function analyze_temps ไปรับ parameter จาก get_temperatures ได้เลยเพราะ return มาเป็น list ละ
display_analysis(avg,high,low)
