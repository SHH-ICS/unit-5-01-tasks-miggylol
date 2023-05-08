import math

# Prompt user for the lengths of the two legs
leg1 = float(input("Enter the length of the first leg: "))
leg2 = float(input("Enter the length of the second leg: "))

# Calculate the length of the hypotenuse
hypotenuse = math.sqrt(leg1**2 + leg2**2)

# Display the result
print(f"The length of the hypotenuse is {hypotenuse}.")
