class Group:
    def __init__(self, name, desc, group_id):
        self.name = name
        self.users = []
        self.desc = desc
        self.group_id = group_id

    def add_users(self, users):
        for user in users:
            self.users.append(user)

    def get_user_list(self):
        return self.users

    def get_group_details(self):
        return self.group_id, self.name, self.desc, self.users
