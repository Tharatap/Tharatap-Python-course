"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input(f"number{i+1} : "))
        numbers.append(number)
      

    # Display original list
    print(f"Original numbers: {sorted(numbers)}")
    # Create filtered lists
    even_numbers = []
    odd_numbers =  []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else :
            odd_numbers.append(numbers[i])
    print(f"even_numbers: {sorted(even_numbers)}")
    print(f"odd_number: {sorted(odd_numbers)}")
  

    # Calculate average
    average = sum(numbers) / 10
  
    # Numbers greater than average
    above_average = []
    for i in range(len(numbers)):
        if numbers[i] > average:
            above_average.append(numbers[i])
    print(f"above_average: {sorted(above_average)}")
    # Your code here
    print(f"Sum: {sum(numbers)}")
    print("average :",average)
    print(f"maxnumber: {max(numbers)}")
    print(f"minnumber: {min(numbers)}")
    
    
if __name__ == "__main__":
    number_operations()