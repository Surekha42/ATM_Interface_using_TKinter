import tkinter as tk
from tkinter import messagebox

# Dummy account for simulation
account = {
    'username': 'surekha',
    'pin': '1234',
    'balance': 1000.0
}

# Main ATM class
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")
        self.root.geometry("400x300")
        self.current_user = None
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="ATM Login", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="PIN:").pack()
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        pin = self.pin_entry.get()
        if username == account['username'] and pin == account['pin']:
            self.current_user = username
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="ATM Main Menu", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Check Balance", command=self.check_balance).pack(pady=5)
        tk.Button(self.root, text="Deposit", command=self.deposit_screen).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_screen).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.create_login_screen).pack(pady=5)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is ₹{account['balance']:.2f}")

    def deposit_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Deposit Amount", font=("Arial", 18)).pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        tk.Button(self.root, text="Deposit", command=self.deposit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            account['balance'] += amount
            messagebox.showinfo("Success", f"₹{amount:.2f} deposited successfully!")
            self.create_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount!")

    def withdraw_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Withdraw Amount", font=("Arial", 18)).pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        tk.Button(self.root, text="Withdraw", command=self.withdraw).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0 or amount > account['balance']:
                raise ValueError
            account['balance'] -= amount
            messagebox.showinfo("Success", f"₹{amount:.2f} withdrawn successfully!")
            self.create_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount or insufficient balance!")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
