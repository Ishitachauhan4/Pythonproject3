import json
from datetime import datetime

# Constants
DATA_FILE = 'expenses.json'

def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category (e.g., food, transportation, entertainment): ").lower()
        date = datetime.now().strftime("%Y-%m-%d")
        
        expenses.append({"amount": amount, "description": description, "category": category, "date": date})
        save_expenses(expenses)
        
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def view_summary(expenses):
    monthly_expenses = {}
    category_expenses = {}
    
    for expense in expenses:
        date = expense["date"]
        amount = expense["amount"]
        category = expense["category"]
        
        month = date[:7]  # Extract YYYY-MM
        
        # Monthly summary
        if month not in monthly_expenses:
            monthly_expenses[month] = 0
        monthly_expenses[month] += amount
        
        # Category summary
        if category not in category_expenses:
            category_expenses[category] = 0
        category_expenses[category] += amount
    
    print("\nMonthly Summary:")
    for month, total in monthly_expenses.items():
        print(f"{month}: ${total:.2f}")
    
    print("\nCategory-wise Summary:")
    for category, total in category_expenses.items():
        print(f"{category}: ${total:.2f}")

def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View summary")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()