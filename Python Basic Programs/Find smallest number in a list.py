# Write a Python program to find smallest number in a list.

# Sample list of numbers
numbers = [30, 10, -45, 5, 20]
# Initialize a variable to store the minimum value, initially set to th
minimum = numbers[0]
# Iterate through the list and update the minimum value if a smaller nu
for i in numbers:
 if i < minimum:
    minimum = i
# Print the minimum value
print("The smallest number in the list is:", minimum)