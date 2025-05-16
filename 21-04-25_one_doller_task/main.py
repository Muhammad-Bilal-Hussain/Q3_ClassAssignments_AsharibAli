from budget_manager import Income, Expense, BudgetManager

def main():
    manager = BudgetManager()

    while True:
        print("==== Personal Budget Manager ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View All Transactions")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            amt = float(input("Enter amount: Rs. "))
            cat = input("Enter category (e.g., Salary, Freelance, Pocket Money): ")
            desc = input("Enter description: ")
            manager.add_transaction(Income(amt, cat, desc))

        elif choice == "2":
            amt = float(input("Enter amount: Rs. "))
            cat = input("Enter category (e.g., Food, Travel, Home Expence, Bike Maintances): ")
            desc = input("Enter description: ")
            manager.add_transaction(Expense(amt, cat, desc))

        elif choice == "3":
            manager.show_summary()

        elif choice == "4":
            manager.show_all_transactions()

        elif choice == "5":
            print("Exiting... Ok Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
