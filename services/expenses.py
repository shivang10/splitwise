from queue import PriorityQueue


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

    def settle_expense(self, all_users):
        per_user_amount = int(self.total_expense / len(all_users))
        users_to_receive_money = {}
        users_to_send_money = {}
        print(per_user_amount, all_users, self.total_expense)
        for user_id in all_users:
            if user_id in self.expenses:
                amount = self.expenses[user_id] - per_user_amount
                if amount < 0:
                    if user_id in users_to_send_money:
                        users_to_send_money[user_id] += amount
                    else:
                        users_to_send_money[user_id] = amount
                elif amount > 0:
                    if user_id in users_to_receive_money:
                        users_to_receive_money[user_id] += amount
                    else:
                        users_to_receive_money[user_id] = amount
            else:
                amount = -per_user_amount
                if amount < 0:
                    if user_id in users_to_send_money:
                        users_to_send_money[user_id] += amount
                    else:
                        users_to_send_money[user_id] = amount
        print(users_to_receive_money)
        print(users_to_send_money)
        self._settle_expense(users_to_send_money, users_to_receive_money)

    def _settle_expense(self, sending_users, receiving_users):
        print("Total expense by the group is: ", self.total_expense)
        send_q = PriorityQueue()
        receive_q = PriorityQueue()
        for user_id in sending_users:
            send_q.put((sending_users[user_id], user_id))

        for user_id in receiving_users:
            receive_q.put((receiving_users[user_id], user_id))

        while send_q.qsize() > 0:
            send_amount, send_user_id = send_q.get()
            receive_amount, receive_user_id = receive_q.get()
            if send_amount + receive_amount == 0:
                print(receive_user_id, " will get", receive_amount, " from ", send_user_id)
            elif send_amount + receive_amount < 0:
                print(receive_user_id, " will get", receive_amount, " from ", send_user_id)
                send_q.put((send_amount + receive_amount, send_user_id))
            elif send_amount + receive_amount > 0:
                print(receive_user_id, " will get", abs(send_amount), " from ", send_user_id)
                receive_q.put((send_amount + receive_amount, receive_user_id))
