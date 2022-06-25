from services.expenses import Expense


class Group:
    def __init__(self, name, desc, group_id):
        self.name = name
        self.users = []
        self.desc = desc
        self.group_id = group_id
        self.expenses = Expense()

    def add_users(self, users):
        for user in users:
            self.users.append(user)

    def get_user_list(self):
        return self.users

    def get_group_details(self):
        return self.group_id, self.name, self.desc, self.users

    def add_expense(self, user_id, amount):
        self.expenses.add_expense(user_id, amount)

    def get_group_expenses(self):
        self.expenses.get_total_expense()

    def get_per_user_expense(self):
        self.expenses.get_per_user_expense()

    def settle_group_expense(self):
        self.expenses.settle_expense(self.users)
