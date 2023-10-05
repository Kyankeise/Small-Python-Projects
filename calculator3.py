# calculator3
# class method
# ============ 

# import some useful packages
# ---------------------------
import os

# define class and associate methods
# ---------------------------------- 
class calculator():

    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def isValid(self):
        if self.num1.isnumeric() and self.num2.isnumeric():
            return True
        else:
            return False
 
    def add(self):
        print( self.num1,"+",self.num2,"=", self.num1 + self.num2 )

    def subtract(self):
        print( self.num1,"-",self.num2,"=", self.num1 - self.num2 )

    def multiply(self):
        print( self.num1,"*",self.num2,"=", self.num1 * self.num2 )

    def divide(self):
        if self.num1 == 0 or self.num2 == 0:   
            print("zero values not allowed in division")
        else:
         print( self.num1,"/",self.num2,"=", self.num1 / self.num2 )


# local function to clear screen
def clearConsole():
    os.system('clear')


# process until user terminates

while True:

    # clear screen
    clearConsole()

    # print menu options
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("9. EXIT")

    # request menu selection from user
    notValid = True
    while notValid:
            select = input("Select an option: ")
            if not select.isnumeric():
                print("Not an integer")
            else:
                select = int(select) #cast, just in case
                notValid = False

    # exit if requested
    if (select == 9):
        break

    # process valid selection
    if (select >= 1) and (select <= 5):

        # input and validate first number
        notValid = True
        while notValid:
            x = input("Enter first number: ")
            if not x.isnumeric():
                print("Not an integer")
            else:
                x = int(x)
                notValid = False

        # input and validate second number
        notValid = True
        while notValid:
            y = input("Enter second number: ")
            if not y.isnumeric():
                print("Not an integer")
            else:
                y = int(y)
                notValid = False

        # create new object from class template
        calc = calculator( x, y)

        if(select == 1):
            calc.add()

        elif(select == 2):
            calc.subtract()

        elif(select == 3):
            calc.multiply()
        
        elif(select == 4):
            calc.divide()

        ignore = input("press any key to continue") 


    else:
        print("invalid selection")

