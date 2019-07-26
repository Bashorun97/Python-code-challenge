'''
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def find_number(first, last):
    arr = [str(i) for i in range(first, last +1) if i%7 == 0 and i%5 != 0]
    return ','.join(arr)

if __name__ == '__main__':
    first, last = 2000, 3200
    print(find_number(first, last))
