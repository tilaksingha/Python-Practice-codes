import tkinter as tk
from tkinter import ttk
# Function to add emoji to current selection
def add_emoji():
# Retrieve the selected emoji name from a combo box.
selected_emoji_name = emoji_combobox.get()
# Find the emoji's symbol based on its name, or say it's not
found."
selected_emoji =
emoji_name_to_unicode.get(selected_emoji_name, "Emoji not
found!")
# Put the selected emoji symbol where the cursor is in the
text box.
text_entry.insert(tk.INSERT, selected_emoji)  # Insert emoji at
current cursor position
# Define a function named print_emoji.
def print_emoji():
# Get the text from the text box, removing any extra spaces
or lines.
printed_text = text_entry.get("1.0", tk.END).strip()
# Update the output label to display the entered text.
output_label.config(text=printed_text)
# Create a window for the Emoji Writer application.
root = tk.Tk()
# Set the title of the window as 'Emoji Writer'.
root.title("Emoji Writer")
# Define categories of emojis with their respective names.
emoji_categories = {
"Smileys & Emotion": ["grinning", "grin", "joy", "rofl",   "sob",
"neutral_face", "smirk", "heart_eyes",
"kissing_heart", "face_with_tears_of_joy",
"rolling_on_the_floor_laughing"],
"Animals & Nature": ["dog", "cat", "mouse", "hamster",
"fox_face", "bear","panda_face", "koala",
"rabbit","tiger", "lion_face",
"horse", "unicorn"],
"Flowers & Fruits" : ["rose","sunflower","tulip","seedling",
"strawberry","melon","cherry","peach",
"mango","pineapple","coconut","kiwi","tomato"]
}
# Create a dictionary mapping emoji names to their Unicode
representations.
emoji_name_to_unicode = {
"grinning": "\U0001F600","grin" : "\U0001F601","joy":
"\U0001F602",  "rofl": "\U0001F923","sob":
"\U0001F62D","neutral_face":"\U0001F610",
"smirk": "\U0001F60F","heart_eyes":
"\U0001F60D","kissing_heart": "\U0001F618",
"face_with_tears_of_joy":
"\U0001F605","rolling_on_the_floor_laughing": "\U0001F923", "dog":
"\U0001F436","cat": "\U0001F431","mouse":
"\U0001F42D","hamster": "\U0001F439",
"fox_face": "\U0001F981","bear": "\U0001F43B","panda_face":
"\U0001F43C","koala": "\U0001F428",
"rabbit": "\U0001F430","tiger": "\U0001F42F","lion_face":
"\U0001F981","horse": "\U0001F434","unicorn": "\U0001F984",
"rose": "\U0001F339","sunflower": "\U0001F33B","tulip":
"\U0001F337","seedling": "\U0001F331",
"strawberry": "\U0001F353","melon": "\U0001F348","cherry":
"\U0001F352","peach": "\U0001F351",
"mango": "\U0001F353","pineapple": "\U0001F348","coconut":
"\U0001F352","kiwi": "\U0001F351","tomato":"\U0001F345"
}
# Create label for title
title_label = tk.Label(root, text="Emoji Printer")
title_label.pack()
title_label.config(fg="yellow", bg="blue", font=("Calibri", 30, "bold"))
# Create label
text_label = tk.Label(root, text="Write your Message :")
text_label.pack()
# Text Entry
text_entry = tk.Text(root, height=3, width=40)
text_entry.pack(pady=10)
# Emoji Selection
emoji_label = ttk.Label(root, text="Select Emoji:")
emoji_label.pack()
# Create a Combobox for emoji selection
# Generate a list of emoji names for the dropdown menu.
# values = list(emoji_name_to_unicode.keys()), It generate list
of emoji names for combobox
# It shows available emoji names and is set to read-only.
emoji_combobox = ttk.Combobox(root,
values=list(emoji_name_to_unicode.keys()), state="readonly")
emoji_combobox.pack()
#  Create a Add Emoji Button
select_button = ttk.Button(root, text="Add Emoji ",
command=add_emoji)
select_button.pack(pady=10)
# Create a Print Message Button
print_button = ttk.Button(root, text="Print Message",
command=print_emoji)
print_button.pack(pady=10)
# Create a Label to display selected emoji
output_label = ttk.Label(root, text="", font=("Helvetica",20),
wraplength=400)
output_label.pack(pady=10)
root.mainloop()