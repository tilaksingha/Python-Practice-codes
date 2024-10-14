import tkinter as tk
import threading
import time
import pyautogui
from pynput import keyboard

# Global variables to control clicking
clicking = False
click_interval = 0

# Function to perform clicking
def click_mouse():
    while clicking:
        pyautogui.click()  # Perform a mouse click
        time.sleep(click_interval)  # Wait for the interval

# Start clicking function
def start_clicking():
    global clicking, click_interval
    # Get input values and convert to seconds
    ms = milliseconds_entry.get()
    s = seconds_entry.get()
    m = minutes_entry.get()
    
    # Calculate total click interval in seconds
    total_seconds = (int(ms) / 1000) + int(s) + (int(m) * 60)
    
    click_interval = total_seconds  # Set the click interval
    clicking = True
    click_thread = threading.Thread(target=click_mouse)
    click_thread.start()  # Start clicking in a new thread

# Stop clicking function
def stop_clicking():
    global clicking
    clicking = False

# Function to set hotkey (example implementation)
def set_hotkey():
    def on_activate_start():
        start_clicking()

    def on_activate_stop():
        stop_clicking()

    # Define hotkeys
    hotkey_start = keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+s': on_activate_start,
        '<ctrl>+<alt>+x': on_activate_stop
    })
    
    hotkey_start.start()  # Start listening for hotkeys
    print("Hotkeys set: Ctrl + Alt + S to Start, Ctrl + Alt + X to Stop")

# Create the main application window
app = tk.Tk()
app.title("AutoClick+ by Tilak")
app.geometry("300x250")  # Set the window size
app.configure(bg="#ffcccb")  # Set a cute reddish background color

# Timer Inputs
tk.Label(app, text="Milliseconds:", bg="#ffcccb").pack(pady=5)
milliseconds_entry = tk.Entry(app)
milliseconds_entry.pack(pady=5)

tk.Label(app, text="Seconds:", bg="#ffcccb").pack(pady=5)
seconds_entry = tk.Entry(app)
seconds_entry.pack(pady=5)

tk.Label(app, text="Minutes:", bg="#ffcccb").pack(pady=5)
minutes_entry = tk.Entry(app)
minutes_entry.pack(pady=5)

# Buttons
tk.Button(app, text="Set Hotkey", command=set_hotkey, bg="#ff9999").pack(pady=5)
tk.Button(app, text="Start", command=start_clicking, bg="#ff9999").pack(pady=5)
tk.Button(app, text="Stop", command=stop_clicking, bg="#ff9999").pack(pady=5)

app.mainloop()
