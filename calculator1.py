# calculator1
# simple version
#===============

# import some useful packages
# ---------------------------
import os

# define functions
# ----------------

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def clearConsole():
    os.system('clear')

# process until user terminates
# -----------------------------

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
    select = int( input("Select an option ") )

    # exit if requested
    if (select == 9):
        break

    # process valid selection
    if (select >= 1) and (select <= 5):

        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        if(select == 1):
            print( x,"+",y,"=", add( x,y) )

        elif(select == 2):
            print( x,"-",y,"=",subtract(x,y))

        elif(select == 3):
            print(x,"x",y,"=",multiply(x,y))

        elif(select == 4):
            print(x,"/",y,"=",divide(x,y))

        ignore = input("press any key to continue") 


    else:
        print("invalid selection. retry")
