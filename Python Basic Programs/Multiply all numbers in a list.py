# Write a Python program to Multiply all numbers in the list.

# Sample list of numbers
numbers = [2, 3, 4, 10]
# Initialize a variable to store the product
product_of_numbers = 1
# Iterate through the list and accumulate the product
for i in numbers:
 product_of_numbers *= i
# Print the product
print("Product of elements in the list:", product_of_numbers)