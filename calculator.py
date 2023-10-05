
#Calculate function - PROCESS

def calculate(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result =  n1*n2
    elif op == '/':
        result = n1/n2
    elif op=='%':
        result =  n1%n2
    else:
        raise ValueError('Invalid operator')
    
        
    return result

#User inputs - INPUT
#Continue Calculating - allow user to calculate a new figure


continue_calculating = True
while continue_calculating is True:
    number1 = float(input('Enter first number: '))
    op = input('Enter operator (+,-,*,/,^): ')
    number2 = float(input('Enter second number: '))
    print(number1,op,number2)
    result=calculate(number1,number2,op)
    print('=',result)
    yes_or_no = input('Continue? (y/n): ')
    if yes_or_no == 'n':
        continue_calculating = False


#Send result to file - OUTPUT
  
print(result)

file_path = "/Users/Kyan/Desktop/answers.txt" 
file = open(file_path, "w")

result_str = str(result)
file.write(result_str)

file.close()