'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class twoMethods():
    def getString(self):
        self.tell = input('Get input: ')

    def printString(self):
        print(self.tell.upper())

instance = twoMethods()
instance.getString()
instance.printString()
