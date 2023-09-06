import csv

# Initialize the CSV file for storing expenses
CSV_FILE = "expense.csv"

# Check if the CSV file exists; if not, create it with headers
def initialize_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
    except FileExistsError:
        pass

# Call the initialization function when the script runs
initialize_csv()

def add_expense(date, category, description, amount):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

def add_expense_menu():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))

    add_expense(date, category, description, amount)
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    print("\nView Expenses")
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            date, category, description, amount = row
            print(f"Date: {date}, Category: {category}, Description: {description}, Amount: {amount}")

def calculate_totals():
    total_daily = 0.0
    total_monthly = 0.0
    total_yearly = 0.0

    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            _, _, _, amount = row
            amount = float(amount)

            # Calculate daily, monthly, and yearly totals
            total_daily += amount
            total_monthly += amount
            total_yearly += amount

    # Display the totals
    print("\nExpense Totals")
    print(f"Daily Total: {total_daily}")
    print(f"Monthly Total: {total_monthly}")
    print(f"Yearly Total: {total_yearly}")

def calculate_totals_menu():
    calculate_totals()

def main_menu():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Totals")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense_menu()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_totals_menu()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option")

if __name__ == "__main__":
    main_menu()
