import tkinter as tk
from tkinter import ttk
from translate import Translator

# Function to perform translation
def translate_text():
    source_text = text_input.get("1.0", tk.END)
    src_lang = source_lang_var.get()
    dest_lang = dest_lang_var.get()
    
    try:
        translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        translation = translator.translate(source_text)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translation)
    except Exception as e:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, f"Error: {e}")

# Function to switch languages
def switch_languages():
    current_src_lang = source_lang_var.get()
    current_dest_lang = dest_lang_var.get()
    source_lang_var.set(current_dest_lang)
    dest_lang_var.set(current_src_lang)

# Create the main application window
root = tk.Tk()
root.title("Offline Translator")
root.geometry("600x400")

# Source Text
text_input_label = tk.Label(root, text="Enter text to translate:")
text_input_label.pack(pady=5)

text_input = tk.Text(root, height=6, width=50)
text_input.pack(pady=5)

# Source Language
src_lang_frame = tk.Frame(root)
src_lang_frame.pack(pady=5)

src_lang_label = tk.Label(src_lang_frame, text="Source Language:")
src_lang_label.pack(side=tk.LEFT)

source_lang_var = tk.StringVar(value="en")

# Radio buttons for language selection
languages = {'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Hindi': 'hi'}
source_lang_menu = ttk.OptionMenu(src_lang_frame, source_lang_var, *languages.keys())
source_lang_menu.pack(side=tk.LEFT)

# Reverse Button
reverse_button = tk.Button(root, text="Reverse", command=switch_languages)
reverse_button.pack(pady=5)

# Destination Language
dest_lang_frame = tk.Frame(root)
dest_lang_frame.pack(pady=5)

dest_lang_label = tk.Label(dest_lang_frame, text="Destination Language:")
dest_lang_label.pack(side=tk.LEFT)

dest_lang_var = tk.StringVar(value="es")
dest_lang_menu = ttk.OptionMenu(dest_lang_frame, dest_lang_var, *languages.keys())
dest_lang_menu.pack(side=tk.LEFT)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=5)

# Output Text
text_output_label = tk.Label(root, text="Translated text:")
text_output_label.pack(pady=5)

text_output = tk.Text(root, height=6, width=50)
text_output.pack(pady=5)

# Run the application
root.mainloop()
