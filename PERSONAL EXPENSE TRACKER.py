import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

#main function 
def create_file():
    """Create CSV file if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    print("\n----- Add Expense -----")

    category = input("Enter category (Food/Travel/Shopping/Education/Medical/Other): ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    print("\n----- All Expenses -----")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        expenses_found = False

        print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
        print("-" * 65)

        for row in reader:
            expenses_found = True
            print(
                f"{row['Date']:<15}"
                f"{row['Category']:<15}"
                f"{row['Description']:<25}"
                f"₹{float(row['Amount']):>9.2f}"
            )

        if not expenses_found:
            print("No expenses found.")


def total_expense():
    print("\n----- Total Expense -----")

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"Total Expense: ₹{total:.2f}")


def category_wise_expense():
    print("\n----- Category-wise Expense -----")

    category_total = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

    if not category_total:
        print("No expenses found.")
        return

    for category, amount in category_total.items():
        print(f"{category}: ₹{amount:.2f}")


def check_budget():
    print("\n----- Budget Check -----")

    try:
        budget = float(input("Enter your monthly budget: ₹"))

        if budget <= 0:
            print("Budget must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid budget.")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    remaining = budget - total

    print(f"Budget: ₹{budget:.2f}")
    print(f"Total Expense: ₹{total:.2f}")

    if remaining > 0:
        print(f"Remaining Budget: ₹{remaining:.2f}")
    elif remaining == 0:
        print("You have used your complete budget.")
    else:
        print(f"Budget Exceeded By: ₹{abs(remaining):.2f}")


def main():
    create_file()

    while True:
        print("\n================================")
        print("   PERSONAL EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Expense")
        print("5. Check Budget")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            category_wise_expense()

        elif choice == "5":
            check_budget()

        elif choice == "6":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


