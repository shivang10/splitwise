class Expense:
    def __init__(self):
        self.expenses = {}
        self.total_expense = 0

    def add_expense(self, user_id, amount):
        if user_id in self.expenses:
            self.expenses[user_id] += amount
        else:
            self.expenses[user_id] = amount

        self.total_expense += amount

    def get_total_expense(self):
        print("total expense is: ", self.total_expense)

    def get_per_user_expense(self):
        for user in self.expenses:
            print(user, self.expenses[user])
