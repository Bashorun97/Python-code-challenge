'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

def generate_list():
    list_hold = [int(i) for i in input().split(',')]
    return list_hold

list_cont = generate_list()
print(list_cont)
print(tuple(list_cont))
