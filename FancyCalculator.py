"""
Andrew Cohen
this is a Fancy ish Calc
accepts one user input, the equation and prints the output
"""
def Fancy_Calculator(equation):

   #display message to user
   print("Hello user, this is a calculator")


   equation = input("provide me with equation:")
   answer = print("Answer: " + str(eval(equation)))  #asks user to enter an equation and provieds an answer

   val1 = print(equation.split(' ')[0])  #pulls from what the user has entered and shows them what was enetered

   return answer


