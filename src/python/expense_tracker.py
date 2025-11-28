class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def get_total(self):
        return sum(item["amount"] for item in self.expenses)

    def show_expenses(self):
        for item in self.expenses:
            print(f"{item['description']}: ${item['amount']:.2f}")
        print(f"Total: ${self.get_total():.2f}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 4.50)
    tracker.add_expense("Lunch", 12.00)
    tracker.show_expenses()
