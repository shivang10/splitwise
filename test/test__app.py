from app import App

# Initialise App
splitwise = App()

# Dummy users data
user1_first_name = "User1"
user1_last_name = "Python"
user1_phone_no = 7574561

user2_first_name = "User2"
user2_last_name = "Rust"
user2_phone_no = 1294561

user3_first_name = "User3"
user3_last_name = "JavaScript"
user3_phone_no = 9456361

user4_first_name = "User4"
user4_last_name = "Scala"
user4_phone_no = 6543161

# Add users
splitwise.add_user(first_name=user1_first_name, last_name=user1_last_name, phone_no=user1_phone_no)
splitwise.add_user(first_name=user2_first_name, last_name=user2_last_name, phone_no=user2_phone_no)
splitwise.add_user(first_name=user3_first_name, last_name=user3_last_name, phone_no=user3_phone_no)
splitwise.add_user(first_name=user4_first_name, last_name=user4_last_name, phone_no=user4_phone_no)

# See users list
splitwise.list_users()

# Dummy group data
group1_name = "group1"
group1_description = "group1_desc"

group2_name = "group2"
group2_description = "group2_desc"

# Add groups
splitwise.add_group(group1_name, group1_description)
splitwise.add_group(group2_name, group2_description)

# List all the groups
splitwise.list_groups()

# To get users and group ids as right now, we are adding every through ids and since ids are
# randomly generated, we don't know their ids. So, here we are fetching the corresponding ids
users_ids = splitwise.get_users_id()
groups_ids = splitwise.get_groups_id()

# Add users to group
splitwise.add_user_to_group(groups_ids[0], users_ids[:3])

# Add expense to the group id with user_id
splitwise.add_expense(groups_ids[0], 20, users_ids[0])
splitwise.add_expense(groups_ids[0], 30, users_ids[1])
splitwise.add_expense(groups_ids[0], 10, users_ids[2])

# List the group expense
splitwise.get_group_expense(groups_ids[0])

# Get expense of every user from the group
splitwise.get_every_user_expense_in_group(groups_ids[0])

# Settle the group expense
splitwise.settle_group_expense(groups_ids[0])
