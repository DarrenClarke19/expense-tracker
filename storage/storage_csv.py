import csv
import os
from datetime import datetime

FILE_PATH = "data/expenses.csv"

def ensure_file_exists():
    """Make sure the CSV file exists with headers."""
    if not os.path.exists(FILE_PATH):
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        with open(FILE_PATH, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "description", "amount", "date"])
            writer.writeheader()

def read_expenses():
    """Read all expenses from the CSV file."""
    ensure_file_exists()
    expenses = []
    with open(FILE_PATH, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append({
                "id": int(row["id"]),
                "description": row["description"],
                "amount": float(row["amount"]),
                "date": row["date"]
            })
    return expenses

def write_expense(description, amount):
    """Add a new expense with an auto-incrementing ID."""
    ensure_file_exists()
    
    # Read existing expenses to get the next ID
    expenses = []
    try:
        with open(FILE_PATH, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["id"]:  # Skip empty rows
                    expenses.append({
                        "id": int(row["id"]),
                        "description": row["description"],
                        "amount": float(row["amount"]),
                        "date": row["date"]
                    })
    except (ValueError, KeyError):
        # If there's an error reading, start fresh
        expenses = []
    
    next_id = 1 if not expenses else max(exp["id"] for exp in expenses) + 1

    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "description", "amount", "date"])
        writer.writerow({
            "id": next_id,
            "description": description,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
    return next_id

def save_expenses(expenses):
    """Save a list of expenses to the CSV file, overwriting existing data."""
    ensure_file_exists()
    with open(FILE_PATH, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "description", "amount", "date"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
