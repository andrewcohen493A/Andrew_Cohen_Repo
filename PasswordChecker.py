"""
Andrew Cohen
Password Checker

runs through the password that will be entered by the user and if the password entered meets the required fields than
password will return secure
"""

def Correct_Password_Response(password):

    symbol = "!@#$%" #sets the required symbols that can be used

    if len(password) >= 8 and True in [num.isdigit() for num in password] and True in [s in symbol for s in password]:
        return input("Secure Password")  #this one statement sets the requirements needed to make a valid password and if everything is true than it is a secure password
    else:
        return input("Not Secure") #anything that is not met will return a not secure password