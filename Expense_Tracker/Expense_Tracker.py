import datetime

class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today()

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_spending_by_category(self):
        spending_by_category = {}
        for expense in self.expenses:
            if expense.category in spending_by_category:
                spending_by_category[expense.category] += expense.amount
            else:
                spending_by_category[expense.category] = expense.amount
        return spending_by_category

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category}")

    def get_total_spending(self):
        return sum(expense.amount for expense in self.expenses)

    def get_average_spending(self):
        return self.get_total_spending() / len(self.expenses)

    def get_spending_by_date(self):
        spending_by_date = {}
        for expense in self.expenses:
            if expense.date in spending_by_date:
                spending_by_date[expense.date] += expense.amount
            else:
                spending_by_date[expense.date] = expense.amount
        return spending_by_date

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def get_expenses_by_date_range(self, start_date, end_date):
        return [expense for expense in self.expenses if start_date <= expense.date <= end_date]

# Usage
tracker = ExpenseTracker()

while True:
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View spending by category")
    print("4. View total spending")
    print("5. View average spending")
    print("6. View spending by date")
    print("7. View expenses by category")
    print("8. View expenses by date range")
    print("9. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date_str = input("Enter date (yyyy-mm-dd) or press enter for today's date: ")
        date = datetime.date.today() if date_str == "" else datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        tracker.add_expense(Expense(amount, category, date))
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        spending_by_category = tracker.get_spending_by_category()
        for category, amount in spending_by_category.items():
            print(f"Category: {category}, Amount: {amount}")
    elif choice == "4":
        print(f"Total spending: {tracker.get_total_spending()}")
    elif choice == "5":
        print(f"Average spending: {tracker.get_average_spending()}")
    elif choice == "6":
        spending_by_date = tracker.get_spending_by_date()
        for date, amount in spending_by_date.items():
            print(f"Date: {date}, Amount: {amount}")
    elif choice == "7":
        category = input("Enter category: ")
        expenses = tracker.get_expenses_by_category(category)
        for expense in expenses:
            print(f"Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category}")
    elif choice == "8":
        start_date_str = input("Enter start date (yyyy-mm-dd): ")
        end_date_str = input("Enter end date (yyyy-mm-dd): ")
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
        expenses = tracker.get_expenses_by_date_range(start_date, end_date)
        for expense in expenses:
            print(f"Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category}")
    elif choice == "9":
        break
    else:
        print("Invalid option. Please choose again.")