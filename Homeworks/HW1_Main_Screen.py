"""
Andrew Cohen
Main screen to call each file
"""
from In_Class_Activities import FancyCalculator


def main():
    program = int(input("Hello, Which program would you like to use Simple Calc(1), Fancy Calc(2), or Password Checker(3): "))

    if program == 1:
        Andrew_Cohen_Calculator.Simple_Calculator()     #set program equal too a number to call a specific program they are trying to use
    elif program == 2:                                  #By also creating if else to run through the 3 different files
        FancyCalculator.Fancy_Calculator()
    elif program == 3:                              #when picking 3 user is given a message to input their password
        password = input("Please enter a password with at least 8 characters, symbol(!@#$%), and a digit: ")
        PasswordChecker.Correct_Password_Response(password) #calls the method and runs through the if statement we made before
        print(password)

if __name__ == "__main__":
     main()