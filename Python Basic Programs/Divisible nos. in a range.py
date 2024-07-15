'''
Create a function that takes three parameters where:
- x is the start of the range (inclusive).
- y is the end of the range (inclusive).
- n is the divisor to be checked against.

Return an ordered list with numbers in the range that are divisible by the third
parameter n.
Return an empty list if there are no numbers that are divisible by n.

Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
'''
def list_operation(x, y, n):
 # Use list comprehension to generate the list of numbers divisible 
 return [num for num in range(x, y + 1) if num % n == 0]
x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
n=int(input("Enter value of n: "))
print(f"The resultant list is : \n{list_operation(x, y, n)}")
