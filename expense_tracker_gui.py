import tkinter as tk
from expense_tracker import add_expense

def add_expense_button_clicked():
    # Capture input from the GUI elements
    date = date_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())

    # Call the add_expense() function with the captured input
    add_expense(date, category, description, amount)

    # Clear the input fields
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create and place GUI elements (labels, entry fields, and buttons)

date_label = tk.Label(root, text="Date:")
date_label.pack()

date_entry = tk.Entry(root)
date_entry.pack()

category_label = tk.Label(root, text="Category:")
category_label.pack()

category_entry = tk.Entry(root)
category_entry.pack()

description_label = tk.Label(root, text="Description:")
description_label.pack()

description_entry = tk.Entry(root)
description_entry.pack()

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

add_button = tk.Button(root, text="Add Expense", command=add_expense_button_clicked)
add_button.pack()

# Start the GUI main loop
root.mainloop()
