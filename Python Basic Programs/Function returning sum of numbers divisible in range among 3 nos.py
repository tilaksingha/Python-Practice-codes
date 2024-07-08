'''
Program 97
Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''

def evenly_divisible(a, b, c):
 total = 0
 for num in range(a, b + 1):
  if num % c == 0:
    total += num
 return total
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
print(f"The required results for the nos. {a}, {b}, {c} is : {evenly_divisible(a, b, c)}")
