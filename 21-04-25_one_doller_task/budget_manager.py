from abc import ABC, abstractmethod

# Abstract Base Class
class Transaction(ABC):
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    @abstractmethod
    def get_type(self):
        pass

# Income Class
class Income(Transaction):
    def get_type(self):
        return "Income"

# Expense Class
class Expense(Transaction):
    def get_type(self):
        return "Expense"

# Main Budget Manager
class BudgetManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print(f"{transaction.get_type()} of Rs. {transaction.amount} added in '{transaction.category}' category.")

    def show_summary(self):
        total_income = sum(t.amount for t in self.transactions if t.get_type() == "Income")
        total_expense = sum(t.amount for t in self.transactions if t.get_type() == "Expense")
        balance = total_income - total_expense

        print("\n===== Monthly Summary =====")
        print(f"Total Income : Rs. {total_income}")
        print(f"Total Expense: Rs. {total_expense}")
        print(f"Net Savings  : Rs. {balance}")
        print("===========================\n")

    def show_all_transactions(self):
        print("\n----- All Transactions -----")
        for t in self.transactions:
            print(f"[{t.get_type()}] Rs. {t.amount} - {t.category} | {t.description}")
        print("-----------------------------\n")
