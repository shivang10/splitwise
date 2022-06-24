from app import App


def main():
    splitwise = App()
    while True:
        print("1 == Add User")
        print("2 == Get Users")
        print("3 == Create Group")
        print("4 == Get Groups")
        print("5 == Add Members to group")
        print("0 == exit")
        operation = int(input())

        if operation == 0:
            print("Closing the app")
            break
        elif operation == 1:
            print("Enter user details")
            first_name = input("Enter first name of user: ")
            last_name = input("Enter last name of user: ")
            phone_no = input("Enter phone number: ")
            splitwise.add_user(first_name, last_name, phone_no)
        elif operation == 2:
            print("All the active users are as follows:")
            splitwise.list_users()
        elif operation == 3:
            print("Enter group details: ")
            name = input("Enter group name: ")
            desc = input("Enter group description: ")
            splitwise.add_group(name, desc)
        elif operation == 4:
            splitwise.list_groups()
        elif operation == 5:
            print("Enter the user_id of users to be added in group")
            print("Enter 0 to exit")
            current_new_users = []
            group_id = input("Enter the group id")
            while True:
                text_input = input("Enter user_id")
                if text_input == "0":
                    break
                else:
                    current_new_users.append(text_input)
            splitwise.add_user_to_group(group_id, current_new_users)


main()
