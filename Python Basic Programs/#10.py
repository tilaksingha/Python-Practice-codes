'''
Create a function that takes a list of numbers between 1 and 10 (excluding one
number) and returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
'''

def missing_num(lst):
 total_sum = sum(range(a, b)) # Sum of numbers from 1 to 10
 given_sum = sum(lst) # Sum of the given list of numbers
 missing = total_sum - given_sum
 return missing

a = int(input("Enter starting no. : "))
b = int(input("Enter ending no. : "))
lst = input("Enter a sequence of whitespace-separated numbers excluding any one number : \n")
words = set(lst.split())
print(f"The excluded no. was : {missing_num(lst)}")