import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# File paths
prev_day = "D:/Coding/Python 2.0/Practice projects/Daily-Expense-manager/Daily Expense Manager/prev_day.txt"
file_path = "D:/Coding/Python 2.0/Practice projects/Daily-Expense-manager/Daily Expense Manager/myfile.txt"

# Today date and day
date = datetime.now().date()
today_day = datetime.now().strftime("%A")

# Check previous day
try:
    with open(prev_day, "r") as f:
        last_date_str = f.read().strip()
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
except FileNotFoundError:
    last_date = None

# New day header
if last_date != date:
    new_day_str = f"""==============================
DAILY EXPENSE RECORD
==============================

Date      : {date}
Day       : {today_day}
"""
    with open(file_path, "a") as f:
        f.write(new_day_str)
    with open(prev_day, "w") as f:
        f.write(str(date))

# List to store expenses
daily_expense = []

# GUI App
root = tk.Tk()
root.title("Daily Expense Manager")
root.geometry("400x400")

# Labels and Entries
labels = ['Item', 'Category', 'Method of Payment', 'Amount', 'Note']
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label.lower()] = entry

# Function to save entry
def save_expense():
    try:
        item = entries['item'].get()
        category = entries['category'].get()
        method = entries['method'].get()
        amount = int(entries['amount'].get())
        note = entries['note'].get()
        time = datetime.now().strftime("%H:%M:%S")
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number!")
        return

    # Record expense
    daily_expense.append(amount)
    expense_str = f"""
----------------------------------
Time    : {time}
Item    : {item}
Category: {category}
Method  : {method}
Amount  : Rs. {amount}
Notes   : {note}
"""
    with open(file_path, "a") as f:
        f.write(expense_str)

    messagebox.showinfo("Saved", "Expense Recorded!")

    # Clear entries
    for entry in entries.values():
        entry.delete(0, tk.END)

# Function to end day and write total
def end_day():
    if not daily_expense:
        messagebox.showinfo("No Data", "No expenses added yet.")
        return

    total = sum(daily_expense)
    with open(file_path, "a") as f:
        f.write("\n----------------------------------\n")
        f.write(f"Total Expenses Today: Rs. {total}\n")
        f.write("----------------------------------\n")
    messagebox.showinfo("Summary", f"Total Expenses Today: Rs. {total}")
    root.quit()

# Buttons
tk.Button(root, text="Add Expense", command=save_expense).grid(row=6, column=0, pady=20)
tk.Button(root, text="End Day", command=end_day).grid(row=6, column=1)

root.mainloop()
