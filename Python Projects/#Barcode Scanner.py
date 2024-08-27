import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from pyzbar.pyzbar import decode

def browse_file():
    # Open file dialog box to select image
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    # Check if an image file is selected
    if filepath:
        # Attempt to open image file
        try:
            # If it is open, extract data from image using decode function
            barcode_data = decode(Image.open(filepath))
            
            # Check if data is properly decoded or not
            if barcode_data:
                # If True, display extracted data on label
                result_label.config(text="Barcode: " + barcode_data[0].data.decode('utf-8'))
            else:
                result_label.config(text="No barcode found in the image.")
        except Exception as e:
            # Error message is displayed when it failed to open file
            messagebox.showerror("Error", "Failed to open image file: " + str(e))

# Create Tkinter window
root = tk.Tk()
root.title("Barcode Scanner")

# Create Label for Project title and apply font style to title label
title_label = tk.Label(root, text="Barcode Scanner", fg="white", bg="Dark Red", font=("Helvetica", 15, "bold"))
title_label.pack(pady=10)

# Create GUI elements
label = tk.Label(root, text="Select Barcode Image:")
label.pack()

# Create Browse button to select input barcode image
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
