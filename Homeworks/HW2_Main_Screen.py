"""
Andrew Cohen
This is the main screen for Homework #2.
"""
# import the necessary files
from Homeworks import HW2


def main():
    """
        The main method.
    """


# Accept password from user
password = input("Give me a password to check")
# Check whether it is a valid password or not
if HW2.ValidLength(password) and HW2.HasNumber(password) and HW2.HasSymbol(password):
    print("Valid password")
else:
    print("Invalid Password")

if __name__ == "__main__":
    main()
