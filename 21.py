'''
Question 21
Level 3

Question��
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
��
The numbers after the direction are steps. Please write a program to 
compute the distance from current position after a sequence of movement
and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be 
assumed to be a console input.
'''

import math

class getDistance:

    def __init__ (self):
        self.cardinal = [0, 0]
    
    def get_coordinates(self):
        
        while True:

            inp1 = input('Enter distance: ')
            if not inp1:
                break
            inp = inp1.split(' ')
            direction, distance = inp[0], int(inp[1])
            if direction == 'UP':
                self.cardinal[0] += distance
                print(self.cardinal)
            elif direction == 'DOWN':
                self.cardinal[0] -= distance
                print(self.cardinal)
            elif direction == 'LEFT':
                self.cardinal[1] -= distance
                print(self.cardinal)
            elif direction == 'RIGHT':
                self.cardinal[1] += distance
                print(self.cardinal)
            else:
                pass
        return self.cardinal
    
    def cal_distance(self):
        distance = int(round(math.sqrt(self.get_coordinates()[0]**2 + self.get_coordinates()[1]**2)))
        return distance

run = getDistance()
print(run.cal_distance())