"""
Andrew Cohen
Main screen to call each file
"""
import Andrew_Cohen_Calculator
import FancyCalculator
import PasswordChecker

def main():
    program = int(input("Hello, Which program would you like to use Simple Calc(1), Fancy Calc(2), or Password Checker(3): "))

    if program == 1:
        Andrew_Cohen_Calculator.Simple_Calculator()     #set program equal too a number to call a specific program they are trying to use
    elif program == 2:                                  #By also creating if else to run through the 3 different files
        FancyCalculator.Fancy_Calculator()
    elif program == 3:
        userpassword = input("Please enter a password with at least 8 characters, symbol(!@#$%), and a digit: ")
        PasswordChecker.Correct_Password_Response(userpassword)

if __name__ == "__main__":
     main()