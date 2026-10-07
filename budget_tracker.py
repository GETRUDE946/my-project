print("=== Budget Tracker ===")


income = 0
expense = 0

try:
    with open("budget_data.txt", "r") as file:
        income = float(file.readline())
        expense = float(file.readline())
except FileNotFoundError:
    pass


while True:
    print("\n1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        new_income = float(input("Enter your income: $"))
        income = income + new_income
        print("Income added:", new_income)

        with open("budget_data.txt", "w") as file:
            file.write(str(income) + "\n")
            file.write(str(expense) + "\n")


    elif choice == "2":
        new_expense = float(input("Enter your expense: $"))
        expense = expense + new_expense
        print("Expense added:", new_expense)

        with open("budget_data.txt", "w") as file:
            file.write(str(income) + "\n")
            file.write(str(expense) + "\n")

    elif choice == "3":
        balance = income - expense

        print("\n=== Budget Summary ===")
        print("Total income:", income)
        print("Total expenses:", expense)
        print("Balance:", balance)

    elif choice == "4":
        print("Thank you for using Budget Tracker!")
        break

    else:
        print("Invalid option. Please choose 1-4.")