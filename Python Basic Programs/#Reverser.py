'''
The "Reverser" takes a string as input and returns that string in reverse order, with
the opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"
reverse("ReVeRsE") ➞ "eSrEvEr"
reverse("Radar") ➞ "RADAr"
'''

def reverse(input_str):
 # Reverse the string and swap the case of characters
 reversed_str = input_str[::-1].swapcase()
 
 return reversed_str

input_str = input("Enter an input string for the Reverser: ")
print(f"Result from the Reverser is :\n {reverse(str)}")