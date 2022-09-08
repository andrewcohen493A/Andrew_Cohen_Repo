"""
Andrew Cohen
simple calc
"""

num1 = 0
num2 = 0


num1 = int(input("What is your first number? "))

num2 = int(input("What is your second number? "))

operation = str(input("Please enter a math operation + - * /: "))

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