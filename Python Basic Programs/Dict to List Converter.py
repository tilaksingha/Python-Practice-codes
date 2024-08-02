'''
Write a function that converts a dictionary into a list of keys-values tuples.
Instructions:
1. Enter the number of key-value pairs you want to add to the dictionary.
2. For each pair, enter the key and value separated by a space.
3. The program will convert the dictionary to a list of tuples and display the result in alphabetical order.

Example:
Input:
3
D 1
B 2
C 3
Output:
[('B', 2), ('C', 3), ('D', 1)]
'''

def dict_to_list():
    # Get the number of key-value pairs
    num_pairs = int(input("Enter the number of key-value pairs: "))

    # Create an empty dictionary
    input_dict = {}

    # Get the key-value pairs from the user
    for _ in range(num_pairs):
        key, value = input("Enter one key and value at a time separated by a space: ").split()
        input_dict[key] = int(value)

    # Sort the dictionary by keys in alphabetical order
    sorted_dict = sorted(input_dict.items())

    # Convert the sorted dictionary to a list of tuples
    result = [(key, value) for key, value in sorted_dict]

    return result

# Call the function and print the result
print(dict_to_list())
