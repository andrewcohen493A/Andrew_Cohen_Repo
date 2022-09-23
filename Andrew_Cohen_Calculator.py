"""
Andrew Cohen
simple calc

This file will run if else statements for when the user inputs 2 seperate variable numbers and the operation they want
to use calculate their problem
"""
def Simple_Calculator():

    num1 = 0
    num2 = 0


    num1 = int(input("What is your first number? ")) #first var

    num2 = int(input("What is your second number? ")) #second var

    operation = str(input("Please enter a math operation + - * /: ")) #operations that will be used to calc

    if operation == '+':
        print("The sum of the two provided values {0}".format(num1),"and {0}".format(num2)," is {0}".format(num1+num2))

    elif operation == '-':
        print("The subtraction of the two provided values {0}".format(num1),"and {0}".format(num2)," is {0}".format(num1-num2))

    elif operation == '*':
        print("The multiplication of the two provided values {0}".format(num1),"and {0}".format(num2)," is {0}".format(num1*num2))

    elif operation == '/':
        print("The division of the two provided values {0}".format(num1),"and {0}".format(num2)," is {0}".format(num1/num2))

    else:
        print("No function was entered")

#used if else statements to run through and check which operation was used and when it checks them it will run that statement and give the answer
