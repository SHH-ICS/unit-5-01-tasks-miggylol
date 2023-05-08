import random

# Prompt user for the range
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))

# Generate random number within the range and display it
random_num = random.randint(range_start, range_end)
print(f"Random number between {range_start} and {range_end}: {random_num}")
