import json
import os
from datetime import datetime

# Load existing expenses
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
else:
    expenses = []

# Add new expenses
n = int(input("How many expenses do you want to enter: "))

for i in range(n):
    amount = float(input(f"Enter amount {i+1}: "))
    category = input("Enter category: ")
    note = input("Enter note (optional): ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    expenses.append(expense)  # Append to the list

# Save back to file
with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=2)  # Save the full list

print("Expenses saved successfully!")
import json

with open("expenses.json", "r") as file:
    expenses = json.load(file)

print("\nYour Saved Expenses:")
for i, expense in enumerate(expenses, 1):
    print(f"\nExpense {i}:")
    print(f"  Amount   : ${expense['amount']}")
    print(f"  Category : {expense['category']}")
    print(f"  Note     : {expense['note']}")
    print(f"  Date     : {expense['date']}")



def show_total_expenses():    #  show total spending.
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    total = sum(expense["amount"] for expense in expenses)
    
    print(f" Total Spending: ${total:.2f}")

show_total_expenses()

def filter_by_category():
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    category_input = input("Enter category to filter by: ").strip().lower()

    filtered = [e for e in expenses 
                if e["category"].strip().lower() == category_input]

    if filtered:
        print(f"\n Expenses in category '{category_input}':")

        for i, e in enumerate(filtered, 1):
            print(f"{i}. ₹{e['amount']} - {e['note']} ({e['date']})")
    else:
        print(f"\n No expenses found in category '{category_input}'")

filter_by_category()

def delete_expenses_by_index():
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    if not expenses:
        print("No expenses to delete.")
        return
    
    print("\nYour Expenses:")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. ₹{e['amount']} - {e['category']} ({e['date']})")

    
    try:
        index = int(input("Enter the expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            with open("expenses.json" , "w") as file:
                json.dump(expenses,file,indent=2)

            print(f"\n Deleted: ₹{deleted['amount']} - {deleted['category']}")

        else:
           print(" Invalid index number.")

    except ValueError:
        print(" Please enter a valid number.")

delete_expenses_by_index()