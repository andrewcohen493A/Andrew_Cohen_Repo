"""
Andrew Cohen
Password Checker
"""

#def Correct_Password_Response(password):

passwordInput = input("provide password: ")
guess = False
while guess is False:
        passwordGuess = input("Ok, what is the reversed password? I will keep asking until you provide the correct answer: ")
        if (''.join(reversed(passwordGuess))) == passwordInput:
            guess = True
            print("You got it!")