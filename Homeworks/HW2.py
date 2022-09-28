"""
Andrew Cohen
HW2
The objective of this program is to utilize HW #1 code to fit into a pre-coded main method
"""

def ValidLength(password):

    # If the password's length is >= 8 return True
    if len(password) >= 8:
        return True

def HasNumber(password):
    # if any number is inputed for the password return True
    if any(char.isdigit() for char in password):
        return True


def HasSymbol(password):
    symbols = ['!', '@', '#', '$', '%']
    # If any symbols specified are inputed than return True
    if any(char in symbols for char in password):
        return True