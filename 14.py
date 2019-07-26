'''
Write a program that accepts a sentence and calculate the
number of upper case letters and lower case let  ters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

def calculate():
    upper, lower = 0, 0
    for i in intake:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower

if __name__ == '__main__':
    intake = input('Enter value: ')
print(calculate(intake))
//
