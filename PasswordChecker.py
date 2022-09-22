"""
Andrew Cohen
Password Checker
"""

def Correct_Password_Response(password):

    lower, upper, symbol, dig = 0, 0, 0, 0  #creating a variable for each requirment and making it zero
    guess = False
    while guess is False:  #runs a loop till the user puts in a correct password
        passwordInput = input("Password does not meet criteria please provide upper case, number, lowercase, and at least 1 symbol !@#$% ")
        if (len(passwordInput) >= 8):   #set lenght for password
            for i in passwordInput:

                # counting lowercase alphabets
                if (i.islower()):    #looks for lower case and adds one so recognize that it has met the requirment same for the rest
                    lower+=1

                # counting uppercase alphabets
                if (i.isupper()):
                    upper+=1

                # counting digits
                if (i.isdigit()):
                    dig+=1

                # counting the mentioned special characters
                if(i=='!'or i=='@' or i=='#' or i=='$' or i=='%'):
                    symbol+=1

        if (lower>=1 and upper>=1 and symbol>=1 and dig>=1 and lower+symbol+upper+dig==len(passwordInput)):
            guess = True
            print("Valid Password")
            # here since we have counted the number of each we set each var >=1 and when the password is entered it runs through the if that was made
        else:
            print("Invalid Password, try again")