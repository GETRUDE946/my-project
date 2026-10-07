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
        while True:
            try:
                new_income = float(input("Enter your income: $"))

                if new_income > 0:
                    break
                else:
                    print("Amount must be greater than 0.")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        income = income + new_income

        with open("budget_data.txt", "w") as file:
            file.write(str(income) + "\n")
            file.write(str(expense) + "\n")

        print("Income added:", new_income)

    elif choice == "2":
        while True:
            try:
                new_expense = float(input("Enter your expense: $"))

                if new_expense > 0:
                    break
                else:
                    print("Amount must be greater than 0.")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        expense = expense + new_expense

        with open("budget_data.txt", "w") as file:
            file.write(str(income) + "\n")
            file.write(str(expense) + "\n")

        print("Expense added:", new_expense)

    elif choice == "3":
        balance = income - expense

        print("\n=== Budget Summary ===")
        print("Total income:", income)
        print("Total expenses:", expense)
        print("Balance:", balance)

        if balance < 0:
            print("You are over budget!")

    elif choice == "4":
        print("Thank you for using Budget Tracker!")
        break

    else:
        print("Invalid option. Please choose 1-4.")