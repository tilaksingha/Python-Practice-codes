'''
Write a program to compress and decompress a string
'''

import zlib
string = input("Enter a string to Compress and Decompress : ")
# Compress the string
compressed_string = zlib.compress(string.encode())
# Decompress the string
decompressed_string = zlib.decompress(compressed_string).decode()
print("Original String:", string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)
