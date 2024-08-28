import tkinter as tk
import random
import time

class AviatorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Aviator Game Simulation")

        # Initial balance
        self.balance = 100000
        self.history = []

        # Set up GUI elements
        self.setup_ui()
    
    def setup_ui(self):
        self.balance_label = tk.Label(self.root, text=f"Balance: ₹{self.balance}", font=("Arial", 16))
        self.balance_label.pack(pady=10)

        self.bet_amount_label = tk.Label(self.root, text="Bet Amount:", font=("Arial", 12))
        self.bet_amount_label.pack()

        self.bet_amount_entry = tk.Entry(self.root)
        self.bet_amount_entry.pack(pady=5)

        self.multiplier_label = tk.Label(self.root, text="Target Multiplier (Auto):", font=("Arial", 12))
        self.multiplier_label.pack()

        self.multiplier_entry = tk.Entry(self.root)
        self.multiplier_entry.pack(pady=5)

        self.normal_bet_button = tk.Button(self.root, text="Place Normal Bet", command=self.place_normal_bet)
        self.normal_bet_button.pack(pady=5)

        self.auto_bet_button = tk.Button(self.root, text="Start Auto Bet", command=self.start_auto_bet)
        self.auto_bet_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.history_label = tk.Label(self.root, text="Last 50 Outputs:", font=("Arial", 12))
        self.history_label.pack()

        self.history_text = tk.Text(self.root, height=10, width=50)
        self.history_text.pack(pady=5)

    def place_normal_bet(self):
        bet_amount = self.get_bet_amount()
        if bet_amount is None or bet_amount > self.balance:
            self.result_label.config(text="Invalid bet amount or insufficient balance.")
            return
        
        multiplier = self.simulate_game()
        self.update_balance(bet_amount, multiplier)
        self.add_to_history(bet_amount, multiplier)

    def start_auto_bet(self):
        bet_amount = self.get_bet_amount()
        target_multiplier = self.get_target_multiplier()
        if bet_amount is None or target_multiplier is None or bet_amount > self.balance:
            self.result_label.config(text="Invalid input or insufficient balance.")
            return
        
        while self.balance >= bet_amount:
            multiplier = self.simulate_game()
            if multiplier >= target_multiplier:
                self.update_balance(bet_amount, multiplier)
                self.result_label.config(text=f"Auto Bet Won! Multiplier: {multiplier}")
                break
            time.sleep(10)  # Wait for 10 seconds before the next auto bet

    def simulate_game(self):
        # Simulate the game. This function returns a random multiplier.
        return round(random.uniform(1.0, 5.0), 2)

    def update_balance(self, bet_amount, multiplier):
        if multiplier > 1:
            win_amount = bet_amount * multiplier
            self.balance += win_amount - bet_amount
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
    root.mainloop()
