import tkinter as tk
from tkinter import scrolledtext
# Define a function called is_palindrome that takes a number n as input.
def is_palindrome(n):
# Convert the number n to a string and check if it's equal to its reverse.
 return str(n) == str(n)[::-1] # Return True if the string representation of n is a palindrome, otherwise return False.
# Define a function called get_palindromes that takes three arguments: min_val, max_val, and option.

def get_palindromes(min_val, max_val, option):
# Create an empty list called palindromes to store palindrome numbers.
 palindromes = []
# Check the value of the option argument.
if option == 1:  # Palindrome divisible by 5
# If option is 1 (Palindrome divisible by 5), iterate through the range of numbers from min_val to max_val.
 for i in range(min_val, max_val + 1):
# If the number is a palindrome and divisible by 5, add it to the palindromes list.
  if is_palindrome(i) and i % 5 == 0:
   palindromes.append(i)
  elif option == 2:  # Square palindrome
# If option is 2 (Square palindrome), iterate through the range of numbers from min_val to max_val.
   for i in range(min_val, max_val + 1):
# If the number is a palindrome and its square root is an integer, add it to the palindromes list.
    if is_palindrome(i) and (i ** 0.5).is_integer():
     palindromes.append(i)
else:  # All palindromes
# If option is neither 1 nor 2, iterate through the range of numbers from min_val to max_val.
 for i in range(min_val, max_val + 1):
# If the number is a palindrome, add it to the palindromes list.
  if is_palindrome(i):
   palindromes.append(i)
# Return the list of palindromes.
 return palindromes
# Define a function called display_palindromes.
def display_palindromes():
# Retrieve the minimum value from the min_entry widget and convert it to an integer.
 min_val = int(min_entry.get())
# Retrieve the maximum value from the max_entry widget and convert it to an integer.
 max_val = int(max_entry.get())
# Retrieve the selected option from the option_var variable.
 option = option_var.get()
# Call the get_palindromes function with the minimum value, maximum value, and selected option, and store the result in the palindromes variable.
palindromes = get_palindromes(min_val, max_val, option)
# Clear the text displayed in the result_text widget.
result_text.delete(1.0, tk.END)
# Iterate through each palindrome in the palindromes list.
for palindrome in palindromes:
# Insert each palindrome followed by a newline character into the result_text widget.
result_text.insert(tk.END, str(palindrome) + '\n')
# Create main window
root = tk.Tk()
root.title("Palindrome Checker")
# Create title label
title_label = tk.Label(root, text="Palindrome Checker and Generator")
title_label.grid(row=0, column=0, columnspan=3, pady=10)
title_label.config(fg="white", bg="Dark Green", font=("Arial", 18,
"bold"))
# Create input fields
min_label = tk.Label(root, text="Min Value:")
min_label.grid(row=1, column=0)
min_entry = tk.Entry(root)
min_entry.grid(row=1, column=1)
max_label = tk.Label(root, text="Max Value:")
max_label.grid(row=2, column=0)
max_entry = tk.Entry(root)
max_entry.grid(row=2, column=1, pady=5)
# Create frame
option_frame = tk.Frame(root)
option_frame.grid(row=3, column=0, columnspan=3, pady=5)
# Create option buttons
option_label = tk.Label(option_frame, text="Options :")
option_label.grid(row=0, column=0)
option_label.config(font=("TkDefaultFont", 10, "bold"))
option_var = tk.IntVar()
option_var.set(0)
option1= tk.Radiobutton(option_frame, text="Palindrome Divisible by
5", variable=option_var, value=1)
option1.grid(row=1, column=0)
option2 = tk.Radiobutton(option_frame, text="Square Palindrome",
variable=option_var, value=2)
option2.grid(row=1, column=1)
option3 = tk.Radiobutton(option_frame, text="All Palindromes",
variable=option_var, value=3)
option3.grid(row=1, column=2)
# Create button to get palindromes
get_palindrome_button = tk.Button(root, text="Get Palindromes",
command=display_palindromes)
get_palindrome_button.grid(row=7, column=0, columnspan=3,
pady=5)
# Create text widget to display results
result_text = scrolledtext.ScrolledText(root, width=50, height=10)
result_text.grid(row=8, column=0, columnspan=2)
root.mainloop()
