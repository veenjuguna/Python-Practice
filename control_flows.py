# Python Control Flow Tutorial for Beginners
# This code demonstrates conditionals (if, elif, else) and loops (for, while)

# 1. Conditionals: Making Decisions
print("=== Conditionals Example ===")
age = int(input("Enter your age: "))
if age >= 18:
    print("You're an adult! You can vote.")
elif age >= 13:
    print("You're a teenager. No voting yet!")
else:
    print("You're a kid. Enjoy childhood!")

    # 2. For Loop: Iterating Over a Sequence
print("\n=== For Loop Example ===")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I love {fruit}!")#it will list all the fruits earlier listed but as an individual.


    # 3. For Loop with Range
print("\n=== For Loop with Range ===")
for i in range(1, 6):  # Counts from 1 to 5
    print(f"Number: {i}")

# 4. While Loop: Repeating Until a Condition is False
print("\n=== While Loop Example ===")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment to avoid infinite loop
    #this counts number one after the other till it gets to 4 because that is less tthan 5

    # 5. Loop Controls: Break and Continue
print("\n=== Break and Continue Example ===")
for i in range(10):
    if i == 5:
        print("Stopping at 5!")
        break  # Exits the loop
    if i % 2 == 0:
        continue  # Skips even numbers
    print(f"Odd number: {i}")

# 6. Mini-Project: Number Guessing Game
print("\n=== Number Guessing Game ===")
import random
secret_number = random.randint(1, 10)
attempts = 0
print("Guess the number between 1 and 10!")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_number:
        print(f"Correct! It took you {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


#if condition:
    # Code to run if condition is True
#elif another_condition:  # Optional
    # Code to run if another_condition is True
#else:  # Optional
    # Code to run if all conditions are False

    #for variable in sequence:
    # Code to run for each item