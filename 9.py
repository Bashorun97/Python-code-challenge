'''
Question
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
def capitalize():
    arr = []
    while True:
        sentInput = input()
        if sentInput:
            arr.append(sentInput)
        else:
            break
    return arr
for i in capitalize():
    print(i.upper())
