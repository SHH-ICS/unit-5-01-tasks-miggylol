import random

# Generate two random numbers between 1 and 100
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Prompt user to answer the addition question
answer = int(input(f"What is {num1} + {num2}? "))

# Check if user's answer is correct and display result
if answer == num1 + num2:
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is {num1 + num2}.")
