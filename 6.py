'''
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
import math

def compute(c, h, seqList):
    value = []
    for p in seqList:
       value.append(str(int(round(math.sqrt(2*c*float(p)/h)))))
       print(value)
    return ','.join(value)

if __name__ == '__main__':
    seqInput = input('Enter input seperated with comma: ')
    seqList = [i for i in seqInput.split(',')]
    print(seqList)
C, H = 50, 30
print(compute(C, H, seqList))
