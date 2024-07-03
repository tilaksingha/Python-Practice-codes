#To display Multiplication Table of a number

num = int(input("Display multiplication table of: "))
upper = int(input("Maximum span of table upto : "))
for i in range(1, upper+1):
 print(f"{num} X {i} = {num*i}")