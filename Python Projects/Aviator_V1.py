import tkinter as tk
import random
import time
import math

class AviatorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Aviator Game Simulation")
        self.root.configure(bg='black')

        # Initial balance
        self.balance = 100000
        self.history = []
        self.is_auto_bet = False
        self.target_multiplier = 1.0
        self.bet_amount = 0
        self.multiplier = 0.75
        self.is_betting = False

        # Set up GUI elements
        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        # Plane emoji as a placeholder
        self.plane_emoji = "✈️"
        self.plane = self.canvas.create_text(50, 300, text=self.plane_emoji, font=("Arial", 24), fill="red")

        self.balance_label = tk.Label(self.root, text=f"Balance: ₹{self.balance}", font=("Arial", 16), fg='red', bg='black')
        self.balance_label.pack(pady=10)

        self.bet_amount_label = tk.Label(self.root, text="Bet Amount:", font=("Arial", 12), fg='red', bg='black')
        self.bet_amount_label.pack()

        self.bet_amount_entry = tk.Entry(self.root)
        self.bet_amount_entry.pack(pady=5)

        self.multiplier_label = tk.Label(self.root, text="Target Multiplier (Auto):", font=("Arial", 12), fg='red', bg='black')
        self.multiplier_label.pack()

        self.multiplier_entry = tk.Entry(self.root)
        self.multiplier_entry.pack(pady=5)

        self.place_bet_button = tk.Button(self.root, text="Place Bet", command=self.place_bet, bg='red', fg='black')
        self.place_bet_button.pack(pady=5)

        self.cashout_button = tk.Button(self.root, text="Cash Out", command=self.cash_out, bg='red', fg='black')
        self.cashout_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), fg='red', bg='black')
        self.result_label.pack(pady=10)

        self.history_label = tk.Label(self.root, text="Last 50 Outputs:", font=("Arial", 12), fg='red', bg='black')
        self.history_label.pack()

        self.history_text = tk.Text(self.root, height=10, width=50)
        self.history_text.pack(pady=5)

        self.watermark = tk.Label(self.root, text="Made by Tilak Singha, ECE, TINT", font=("Arial", 10), fg='red', bg='black')
        self.watermark.place(x=600, y=550)

        # Canvas for bet info
        self.bet_info = self.canvas.create_text(400, 50, text=f"Current Bet: ₹{self.bet_amount}", font=("Arial", 18), fill="red")

        # Update the GUI to show current bet amount
        self.root.after(100, self.update_bet_info)

    def update_bet_info(self):
        self.canvas.itemconfig(self.bet_info, text=f"Current Bet: ₹{self.bet_amount}")
        self.root.after(100, self.update_bet_info)

    def place_bet(self):
        self.bet_amount = self.get_bet_amount()
        if self.bet_amount is None or self.bet_amount > self.balance:
            self.result_label.config(text="Invalid bet amount or insufficient balance.")
            return

        self.is_betting = True
        self.canvas.delete("all")
        self.canvas.create_text(50, 300, text=self.plane_emoji, font=("Arial", 24), fill="red")

        self.plane_trajectory = []
        self.multiplier = 0.75

        self.update_game()

    def cash_out(self):
        if not self.is_betting:
            self.result_label.config(text="No active bet to cash out.")
            return

        self.is_betting = False
        self.canvas.delete("all")
        self.canvas.create_text(50, 300, text=self.plane_emoji, font=("Arial", 24), fill="red")
        self.update_balance(self.bet_amount, self.multiplier)
        self.result_label.config(text=f"Cashed Out! Multiplier: {self.multiplier}")
        self.add_to_history(self.bet_amount, self.multiplier)

    def update_game(self):
        start_time = time.time()
        flight_duration = 10  # Duration for the plane to complete its flight
        frame_rate = 30  # Frames per second

        while time.time() - start_time < flight_duration and self.is_betting:
            self.canvas.delete("trajectory")
            self.multiplier = round(random.uniform(0.75, 500.0), 2)
            elapsed_time = (time.time() - start_time)
            progress = elapsed_time / flight_duration

            # Random increasing trajectory
            curve = 100 * math.sin(2 * math.pi * progress) + 300
            self.plane_x = 50 + (750 * progress)
            self.plane_y = curve

            # Draw dotted trajectory
            if self.plane_trajectory:
                self.canvas.create_oval(self.plane_x, self.plane_y, self.plane_x+2, self.plane_y+2, fill='red', outline='red')

            self.plane_trajectory.append((self.plane_x, self.plane_y))
            self.canvas.create_text(400, 50, text=f"Multiplier: {self.multiplier}", font=("Arial", 18), fill="red")

            self.root.update()
            time.sleep(1 / frame_rate)

        if self.is_betting:
            self.update_balance(self.bet_amount, 0)
            self.result_label.config(text=f"Flew Away! Multiplier: {self.multiplier}")
            self.add_to_history(self.bet_amount, self.multiplier)

    def update_balance(self, bet_amount, multiplier):
        if multiplier > 0:
            if multiplier > 1:
                win_amount = bet_amount * multiplier
                self.balance += win_amount - bet_amount
            else:
                self.balance -= bet_amount
        else:
            self.balance -= bet_amount

        self.balance_label.config(text=f"Balance: ₹{self.balance}")

    def add_to_history(self, bet_amount, multiplier):
        self.history.append((bet_amount, multiplier))
        if len(self.history) > 50:
            self.history.pop(0)

        self.history_text.delete(1.0, tk.END)
        for bet, mult in self.history:
            self.history_text.insert(tk.END, f"Bet: ₹{bet} | Multiplier: {mult}\n")

    def get_bet_amount(self):
        try:
            return float(self.bet_amount_entry.get())
        except ValueError:
            return None

    def get_target_multiplier(self):
        try:
            return float(self.multiplier_entry.get())
        except ValueError:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    game = AviatorGame(root)
    root.mainloop()a
