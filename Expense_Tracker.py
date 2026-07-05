"""
Expense Tracker

A simple command-line expense tracker.

Features:
- Add expenses
- View all expenses
- View total expenses
- Stores data in a text file

Skills Used:
- Dictionaries
- Loops
- File Handling
- Exception Handling
"""

expenses = {}

while True:
    print("\n========== Expense Tracker ==========")
    print("1. Enter Expenses")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nEnter the expense and amount below\n")

            n = int(input("How many expenses do you want to enter? "))

            for i in range(n):
                exp = input("Enter expense name: ").title()
                amt = int(input("Enter amount: "))

                if amt < 0:
                    print("Amount cannot be negative!")
                    continue

                if exp in expenses:
                    expenses[exp] += amt
                else:
                    expenses[exp] = amt

            with open("expenses.txt", "w") as file:
                for exp, amt in expenses.items():
                    file.write(f"{exp}:{amt}\n")

            print("\nExpenses saved successfully!")

        elif choice == 2:

            print("\n------ Expense List ------")

            try:
                with open("expenses.txt", "r") as file:

                    empty = True

                    for line in file:
                        print(line.strip())
                        empty = False

                    if empty:
                        print("No expenses found.")

            except FileNotFoundError:
                print("No expense file found.")

        elif choice == 3:

            print("\n------ Total Expenses ------")

            total = 0

            try:
                with open("expenses.txt", "r") as file:

                    for line in file:
                        amt = int(line.strip().split(":")[1])
                        total += amt

                print(f"Total Spent: ₹{total}")

            except FileNotFoundError:
                print("No expense file found.")

        elif choice == 4:
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Please enter a valid option (1-4).")

    except ValueError:
        print("Invalid input! Please enter numbers only.")