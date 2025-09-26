import tkinter as tk
from tkinter import messagebox

accounts = {}

def create_account():
    username = entry_user.get()
    if username in accounts:
        messagebox.showerror("Error", "Account already exists!")
    else:
        accounts[username] = 0.0
        messagebox.showinfo("Success", f"Account created for {username} with balance ₦0.0")

def deposit():
    username = entry_user.get()
    amount = entry_amount.get()
    if username not in accounts:
        messagebox.showerror("Error", "Account does not exist!")
        return
    try:
        amount = float(amount)
        accounts[username] += amount
        messagebox.showinfo("Success", f"₦{amount} deposited.\nNew Balance: ₦{accounts[username]}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount!")

def withdraw():
    username = entry_user.get()
    amount = entry_amount.get()
    if username not in accounts:
        messagebox.showerror("Error", "Account does not exist!")
        return
    try:
        amount = float(amount)
        if accounts[username] >= amount:
            accounts[username] -= amount
            messagebox.showinfo("Success", f"₦{amount} withdrawn.\nNew Balance: ₦{accounts[username]}")
        else:
            messagebox.showerror("Error", "Insufficient balance!")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount!")

def check_balance():
    username = entry_user.get()
    if username in accounts:
        messagebox.showinfo("Balance", f"{username}'s Balance: ₦{accounts[username]}")
    else:
        messagebox.showerror("Error", "Account does not exist!")


root = tk.Tk()
root.title("Basic Banking System")


tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Amount (₦):").grid(row=1, column=0, padx=10, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=1, column=1, padx=10, pady=5)


tk.Button(root, text="Create Account", command=create_account).grid(row=2, column=0, pady=5)
tk.Button(root, text="Deposit", command=deposit).grid(row=2, column=1, pady=5)
tk.Button(root, text="Withdraw", command=withdraw).grid(row=3, column=0, pady=5)
tk.Button(root, text="Check Balance", command=check_balance).grid(row=3, column=1, pady=5)

root.mainloop()