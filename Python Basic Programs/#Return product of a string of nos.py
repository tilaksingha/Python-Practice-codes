'''
Needs to be edited when online

Given a string of numbers separated by a comma and space, return the product of
the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20
'''

def multiply_nums(nums_str):
 # Split the input string by comma and space, then convert to intege
 nums = [int(num) for num in nums_str.split(", ")]
 
 # Initialize the result with 1
 result = 1
 
 # Multiply all the numbers together
 for num in nums:
  result *= num
 
 return result

nums_str = set(input("Enter a list of numbers separated by a comma and a space: "))
print(multiply_nums(nums_str))

multiply_nums("1, 2, 3, 4")
multiply_nums("54, 75, 453, 0")
multiply_nums("10, -2")