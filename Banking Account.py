import tkinter as tk
from tkinter import messagebox

class BankingApp:
    def __init__(self):
        self.balance = 0
        
        #Main window
        self.window = tk.Tk()
        self.window.title("Banking App")
        self.window.geometry("300x400")
        self.window.configure(bg="#c5e1ff")  # Darker blue background
        
        #Title
        tk.Label(
            self.window,
            text="My Bank",
            font=("Arial", 20, "bold"),
            bg="#c5e1ff",
            fg="#1a365d"  # Dark blue text
        ).pack(pady=20)
        
        #Balance display
        self.balance_label = tk.Label(
            self.window,
            text=f"Balance: ${self.balance:.2f}",
            font=("Arial", 14),
            bg="#c5e1ff",
            fg="#1a365d"
        )
        self.balance_label.pack(pady=10)
        
        #Amount entry
        tk.Label(
            self.window,
            text="Enter amount:",
            bg="#c5e1ff",
            fg="#1a365d"
        ).pack()
        
        self.amount_entry = tk.Entry(
            self.window,
            width=20,
            font=("Arial", 12),
            justify='center'
        )
        self.amount_entry.pack(pady=5)
        
        def create_button(text, command):
            return tk.Button(
                self.window,
                text=text,
                command=command,
                width=15,
                font=("Arial", 10, "bold"),
                bg="#2874A6",  # Button color
                fg="black",    # Button text color
                relief="raised",
                bd=3,
                pady=5
            )
        
        create_button("Deposit", self.deposit).pack(pady=8)
        create_button("Withdraw", self.withdraw).pack(pady=8)
        create_button("Exit", self.window.destroy).pack(pady=15)

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
        self.amount_entry.delete(0, tk.END)

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount")
                return None
            return amount
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return None

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            self.balance += amount
            self.update_balance()
            messagebox.showinfo("Success", f"Deposited ${amount:.2f}")

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.balance -= amount
                self.update_balance()
                messagebox.showinfo("Success", f"Withdrawn ${amount:.2f}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BankingApp()
    app.run()