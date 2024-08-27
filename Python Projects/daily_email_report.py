import tkinter as tk
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

# Create the main application window
root = tk.Tk()
root.title("Offline Translator")

# Source Text
text_input_label = tk.Label(root, text="Enter text to translate:")
text_input_label.pack()

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Source Language
src_lang_label = tk.Label(root, text="Source Language (e.g., 'en' for English):")
src_lang_label.pack()

source_lang_var = tk.StringVar(value="en")
source_lang_entry = tk.Entry(root, textvariable=source_lang_var)
source_lang_entry.pack()

# Destination Language
dest_lang_label = tk.Label(root, text="Destination Language (e.g., 'es' for Spanish):")
dest_lang_label.pack()

dest_lang_var = tk.StringVar(value="es")
dest_lang_entry = tk.Entry(root, textvariable=dest_lang_var)
dest_lang_entry.pack()

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Output Text
text_output_label = tk.Label(root, text="Translated text:")
text_output_label.pack()

text_output = tk.Text(root, height=10, width=50)
text_output.pack()

# Run the application
root.mainloop()
