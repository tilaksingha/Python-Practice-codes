'''
Needs to be corrected when online


An isogram is a word that has no duplicate letters. Create a function that takes a
string and returns either True or False depending on whether or not it's an "isogram".

Examples
is_isogram("Algorism") ➞ True
is_isogram("PasSword") ➞ False
- Not case sensitive.
is_isogram("Consecutive") ➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.
'''

def is_isogram(word):
 
 word = word.lower()
 # Create a set to store unique letters in the word
 unique_letters = set()
 for letter in word:
 # If the letter is already in the set, it's not an isogram
  if letter in unique_letters:
   return False
 # Otherwise, add it to the set
  else:
   unique_letters.add(letter)
   return True

word=str(input("Enter a One-Word String: "))
print(f"{is_isogram(word)}")