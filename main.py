from app import App


def main():
    splitwise = App()
    while True:
        print("1 == Add User")
        print("2 == Get Users")
        print("3 == Create Group")
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


main()
