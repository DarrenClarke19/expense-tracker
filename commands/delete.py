from storage.storage_csv import read_expenses, save_expenses

def run(expense_id):
    """Delete expense by ID."""
    expenses = read_expenses()
    new_expenses = [e for e in expenses if e["id"] != expense_id]
    if len(expenses) == len(new_expenses):
        print("Error: Expense ID not found")
    else:
        save_expenses(new_expenses)
        print("Expense deleted successfully")
