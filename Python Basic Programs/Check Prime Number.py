# Write a Python program to check if a number is Prime Number 

num = int(input("Enter a number: "))
# define a flag variable
flag = False
if num == 1:
 print(f"{num}, is not a prime number")
elif num > 1:
 # check for factors
 if flag == False:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True # if factor is found, set flag to True
    # check if flag is True
    if flag == False:
        print(f"{num}, is a prime number")
    else:
        print(f"{num}, is not a prime number")