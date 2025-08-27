from storage.storage_csv import read_expenses

def run(month=None):
    """Summarize expenses (all or by month)."""
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    if month:
        filtered = [e for e in expenses if int(e["date"].split("-")[1]) == month]
        total = sum(e["amount"] for e in filtered)
        print(f"Total expenses for month {month}: ${total:.2f}")
    else:
        total = sum(e["amount"] for e in expenses)
        print(f"Total expenses: ${total:.2f}")
