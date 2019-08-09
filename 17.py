'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
��
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
def balance():
    bal = 0
    while True:
        inp = input('Enter amount: ')
        if not inp:
            break
        transaction = inp.split(' ')
        action, amount = transaction[0], int(transaction[1])
        if action == 'D':
            bal += amount
        elif action == 'W':
            bal -= amount
    return bal
print(balance())