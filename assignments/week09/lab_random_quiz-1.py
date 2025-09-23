"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random
def Game_Guess_number():
    random_number = random.randint(1,20)
    Heart = 6 # เอาไว้ใช้เก็บค่าโอกาสทายผิด หรือเป็น หัวใจนั้นเอง
    guess = 0 # เอาไว้ใช้เก็บรอบในการทายคำแต่ละครั้ง
    print("=== SIMPLE GUESSING GAME ===")
    print("You have 6 attempts.")
    while Heart != 0:
        number = int(input("  Guess my number between 1 and 20!  : "))
        guess += 1 
        if Heart != 0: # เช็คหัวใจไม่ให้เท่ากับ 0
            print(f"Attempt {guess}/6 your guess: {number}")
        if number == random_number: # check win
            print(f"Congratulations! You won in {guess} attempts!")
            break
        elif number > random_number: # check more
            print("Too high! Try again.")
            Heart -= 1
        else: # check less
            print("Too low! Try again.")
            Heart -= 1
    if Heart == 0:
        print("Game Over you loss")
Game_Guess_number()