"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""

import random

def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even" 
    else:
        return "HINT: The number is odd"

def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
    # ใช้ขอบล่างเป็น = number-10    ขอบบนเป็น =  number +15 
    #ขอบล่าง
    if number > 0 and number >= 10: # ถ้าเป็นเลข หลักหน่วยมันจะลบ 10 เป็นขอบล่างติดลบไม่ได้ 
        current_min = number -10
    #ขอบบน
    if number <= 85: # ถ้าเป็นเลข 90 กว่าๆมันจะเกินร้อยไม่ได้
        current_max = number + 15
    print(f"range: {current_min} - {current_max}") 
    

def get_thefirst_digit_hint(number):
    if number % 100 == 0: # มันคือเลข100 เพราะเราสุ่ม 1 - 100
        print(f"First Digit:{number//100} ")
    elif number % 100 == number: # check ว่าเป็นหลัก 10 
        print(f"First Digit:{number // 10}")
    else: # มันเป็นหลักหน่วย   (แต่ถ้าใบ้หลักหน่วยมันเหมือนเฉลยเพราะมีหลักเดียว)
        print(f"First Digit:{number // 1}")
def Game_random_number():
    random_number = random.randint(1,100)
    guess = 0
    print(f"=== Enhanced GUESSING GAME ===")
    print(f"Guess my number between 1 and 100!")
    print(f"Unlimited attempts")
    while True:
        number = int(input(" Guess my number between 1 and 100!  :"))
        guess += 1 
        print(f"Attempt {guess} your guess: {number}")
        if number == random_number: # check win
            print(f"Congratulations! You won in {guess} attempts!")
            break
        elif number > random_number: # check more
            print("Too high! Try again.")
        else: # check less
            print("Too low! Try again.")
        if guess == 3:
            print("=== Hint ===") # เลขคู่ or คี่
            print(get_parity_hint(random_number))

        elif guess == 5:
            print("=== Hint ===")  # หาร 3 หรือ 5 ลงตัวไหม
            print(get_divisibility_hint(random_number))

        elif guess == 7:
            print("=== Hint ===") # rang_number
            get_range_hint(random_number)

        elif guess == 10:
            print("=== Hint ===") # first_Digit
            get_thefirst_digit_hint(random_number)
Game_random_number()

