'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''

class Generator:

    def __init__ (self):
        self.iterate = int(input('Enter number: '))
    
    def get_values(self):
        for i in range(0, self.iterate + 1):
            if i % 7 == 0:
                yield i
                
    def generate(self):
        for i in self.get_values():
            print (i)

run = Generator()
print(run.generate())