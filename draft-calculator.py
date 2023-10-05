#User input 


a = float(input("Enter the first number"))
b = float(input("enter the second number"))



# operator list
print("""
1.Add
2. Subtraction
3. Multiply
4.Divide
5. Modulus
""")

#User select option

option = int(input("Enter the chosen number:"))

#perform calculations based on input number



if option == 1:
    print("Add: {} + {} = {}".format(a,b,a+b))
elif option == 2:
    print("Subtract: {} - {} = {}".format(a,b,a-b))
elif option == 3:
    print("Multiply: {} * {} = {}".format(a,b,a*b))
elif option == 4:
    print("Divide: {} / {} = {}".format(a,b,a/b))
elif option == 5:
    try:
        print("Modulus: {} / {} = {} Remainder: {}" .format(a,b,a//b,a%b))
    except:
        print("Error. Division by 0 not possible please try again")

    else:
        print("No such choice")















