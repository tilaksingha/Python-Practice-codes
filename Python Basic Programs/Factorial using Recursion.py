'''
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
'''

def factorial(n):
 if n == 0:
  return 1 # Base case: factorial of 0 is 1
 else:
  return n * factorial(n - 1) # Recursive case: n! = n * (n-1)!

n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")