from models.users import User
from models.id_generator import IdGenerate
from models.groups import Group


class App:
    def __init__(self):
        self.users = {}
        self.groups = {}

    def add_user(self, first_name, last_name, phone_no):
        new_user_id = IdGenerate().id_generated
        self.users[new_user_id] = User(first_name, last_name, phone_no, new_user_id)

    def add_group(self, name, desc):
        new_group_id = IdGenerate().id_generated
        self.groups[new_group_id] = Group(name, desc, new_group_id)

    def add_user_to_group(self, group_id, current_new_users):
        self.groups[group_id].add_users(current_new_users)

    def list_users(self):
        for user in self.users:
            print(self.users[user].first_name, self.users[user].phone_no)

    def list_groups(self):
        for group in self.groups:
            print(self.groups[group].name, self.groups[group].desc, self.groups[group].group_id)

    def get_group_details(self, group_id):
        for user in self.groups[group_id]:
            print(user.first_name, user.last_name, user.user_id)

    def get_users_id(self):
        users_ids = []
        for user in self.users:
            users_ids.append(self.users[user].user_id)
        return users_ids

    def get_groups_id(self):
        groups_ids = []
        for group in self.groups:
            groups_ids.append(self.groups[group].group_id)
        return groups_ids

    def add_expense(self, group_id, amount, user_id):
        self.groups[group_id].add_expense(user_id, amount)

    def get_group_expense(self, group_id):
        self.groups[group_id].get_group_expenses()

    def get_every_user_expense_in_group(self, group_id):
        self.groups[group_id].get_per_user_expense()

    def settle_group_expense(self, group_id):
        self.groups[group_id].settle_group_expense()
