# Splitwise App

It is an expense sharing application is where you can add your expenses and split it among different people.
The app keeps balances between people as in who owes how much to whom.
There are various operations that can be performed.

- Add user
- Create group
- Add user to group
- Enter expense details along with user_id and group_id
- See all the group members
- See expense of the group
- See expense of every user of the group
- Settle group expense

To run the application, simply execute the main.py file. It will show all the operations'
user can perform. There is one test__app.py file as a sample input that can help you understand
how to execute commands.

### Algorithm

1. Every group, expense is stored as key: value pair, where key is user_id and value is total amount
   spent by the user.
2. Every time someone pays, that amount is added to user's expense as well as total
   group expense.
3. To settle expense, amount per user is calculated.
4. After that, for every user, it is checked if user has paid any amount or not. If it has paid, then the
   remaining amount is assigned to that user and that can be either positive (user will receive amount) or
   negative (user will give amount, though user paid, but it may turn out that the amount per user was higher than what
   the
   user paid). If the user has not paid any amount, then it is simply assigned the amount to be paid.
5. The amount to be paid by user is stored in priority queue data structure as (amount,user_id). Same applies for amount
   to be received by the user
6. The loop is run until the priority queue becomes empty.
7. The amount to be sent will always be equal to amount to be received.
8. Highest amount to be paid is canceled along with the highest amount to be received and correspondingly is added to
   send/receive
   queue.

