from storage.storage_csv import read_expenses

def run():
    """List all expenses in a formatted table."""
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("ID  Date       Description      Amount")
    for e in expenses:
        print(f"{e['id']:2}  {e['date']}  {e['description']:<15} ${e['amount']:.2f}")
