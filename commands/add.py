from datetime import date
from storage.storage_csv import read_expenses, write_expense

def run(description, amount):
    """Add a new expense with description + amount."""
    expenses = read_expenses()
    expense_id = write_expense(description, amount)
    print(f"Expense added successfully (ID: {expense_id})")
