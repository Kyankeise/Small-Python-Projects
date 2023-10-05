# calculator2
# with input validation
# =====================

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
    # ------------------
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("9. EXIT")

    # request menu selection from user
    # --------------------------------
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
    # -----------------------
    if (select >= 1) and (select <= 5):

        # input and validate first number
        # -------------------------------
        notValid = True
        while notValid:
            x = input("Enter first number: ")
            if not x.isnumeric():
                print("Not an integer")
            else:
                x = int(x)
                notValid = False

        # input and validate second number
        # --------------------------------
        notValid = True
        while notValid:
            y = input("Enter second number: ")
            if not y.isnumeric():
                print("Not an integer")
            else:
                y = int(y)
                notValid = False

        # special valdation for divide, can't have zero
        # ---------------------------------------------
        if(select == 4):
            if x == 0 or y == 0:
                print( "**serious error - can't divide by zero")

        else:

            if(select == 1):
                print( x,"+",y,"=", add(x,y) )

            elif(select == 2):
                print(x,"-",y,"=",subtract(x,y))

            elif(select == 3):
                print(x,"*",y,"=",multiply(x,y))

            elif(select == 4):
                print(x,"/",y,"=",divide(x,y))

        ignore = input("press any key to continue") 


    else:
        print("invalid selection")

