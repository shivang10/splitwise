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
            print(self.groups[group].name, self.groups[group].desc, self.groups[group.group_id])

    def get_group_details(self, group_id):
        for user in self.groups[group_id]:
            print(user.first_name, user.last_name, user.user_id)
