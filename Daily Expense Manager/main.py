from datetime import datetime

# previous day file for maintaining record or new day to print new_day_str
prev_day = "D:/Coding/Python 2.0/Practice projects/Daily-Expense-manager/Daily Expense Manager/prev_day.txt"
file_path = "D:/Coding/Python 2.0/Practice projects/Daily-Expense-manager/Daily Expense Manager/myfile.txt"
# Today date and day
date = datetime.now().date()
today_day = datetime.now().strftime("%A")

# checking previous day date
try:
    with open(prev_day, "r") as f:
        last_date_str = f.read().strip()
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
except FileNotFoundError:
    last_date = None

# Write new day header if new day
if last_date != date:
    new_day_str = f"""==============================
DAILY EXPENSE RECORD
==============================

Date      : {date}
Day       : {today_day}
"""
    with open(file_path, "a") as f:
        f.write(new_day_str)
    # update the date
    with open(prev_day, "w") as f:
        f.write(str(date))

daily_expense = list()
# Loop for repeating the program
while True:
    # Local time
    loc_time = datetime.now().strftime("%H:%M:%S") 
    item = str(input("Enter the item you spend money on: "))
    category = str(input("Enter the category of item: "))
    method = str(input("Enter the mode of payment: "))
    try:
        exp = int(input("Enter the money you spent: "))
    except ValueError:
        print("Invalid amount! Try again.")
        continue
    note = str(input("Enter a note: "))

    # Append expense to list
    daily_expense.append(exp)

    # Expence str for maintaining record and presentation
    expence = f"""
----------------------------------
Time    : {loc_time}
Item    : {item}
Category: {category}
Method  : {method}
Amount  : Rs. {exp}
Notes   : {note}
"""
    # file handeling for storing expence
    with open(file_path, "a") as f:
        f.write(expence)

    # Ask user if they want to continue
    cont = input("Add another expense? (y/n): ").lower()
    if cont != "y":
        break


# End of day summary
with open(file_path, "a") as f:
    f.write("\n----------------------------------\n")
    f.write(f"Total Expenses Today: Rs. {sum(daily_expense)}\n")
    f.write("----------------------------------\n")
    