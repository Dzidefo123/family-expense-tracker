import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

# Create an 'expenses' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
     )
''')

# Save the changes and close the connection
conn.commit()
conn.close()

def add_expense(date, category, description, amount):
    # Connect to the SQLite database
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    
    # Insert the expense data into the 'expenses' table
    cursor.execute('''
        INSERT INTO expenses (date, category, description, amount)
        VALUES (?, ?, ?, ?)
    ''', (date, category, description, amount))
    
    # Save the changes and close the connection
    conn.commit()
    conn.close()
    
def view_expenses():
    # Connect to the SQLite database
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    
    # Retrieve and display all expenses
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    
    print("\nView Expenses")
    for expense in expenses:
        id, date, category, description, amount = expense
        print(f"ID: {id}, Date: {date}, Category: {category}, Description: {description}, Amount: {amount}")
    
    # Close the connection
    conn.close()
    
def calculate_totals():
    # Connect to the SQLite database
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    
    # Calculate daily, monthly, and yearly totals
    cursor.execute('SELECT SUM(amount) FROM expenses WHERE date = DATE()')
    daily_total = cursor.fetchone()[0]
    
    cursor.execute('SELECT SUM(amount) FROM expenses WHERE strftime("%Y-%m", date) = strftime("%Y-%m", DATE())')
    monthly_total = cursor.fetchone()[0]
    
    cursor.execute('SELECT SUM(amount) FROM expenses WHERE strftime("%Y", date) = strftime("%Y", DATE())')
    yearly_total = cursor.fetchone()[0]
    
    # Display the totals
    print("\nExpense Totals")
    print(f"Daily Total: {daily_total}")
    print(f"Monthly Total: {monthly_total}")
    print(f"Yearly Total: {yearly_total}")
    
    # Close the connection
    conn.close()

def main_menu():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Totals")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            # Collect input from the user for adding an expense
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            
            # Call the add_expense() function with the collected input
            add_expense(date, category, description, amount)
            
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_totals()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option")

if __name__ == "__main__":
    main_menu()