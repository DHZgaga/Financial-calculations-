""" 
start

Ask for input from the user

Define what the viable answers are

if the wrong answer is input, print the error message

if the input is one of the viable answers continue

  create 2 lists, for 2 sets of variable options (investment and bond)

   if input is for investment:

      ask for input on simple or compound iterest
      define variables, put them into integers and ask for input from the user

      depending on which interest is chosen, calculate the amount
      print out the result (with a f-string so the answer is a string)

   if input is for bond:
      define variables, put them into integers and ask the user for input
      print out the result (in f-string)

      stop
      
"""
import math
user_decision = input("Which financial calculation would you like to choose? Investment or bond?\
                      \n Investment is used to calculate the amount of interest you'll earn on your investment.\
                      \n Bond is used to calculate the amount you'll have to pay on a home loan.\
                      \n Please enter either 'bond' or 'investment': ")
viable_options = ["Investment", "investment", "INVESTMENT", "Bond", "bond", "BOND"]
# '\' can be used to have the string in next line on the coding side, whereas '\n' will show it in a new line in output side
if user_decision not in viable_options: # If the user chooses anything else but the 6 options in the above variable:
    print("Sorry, this is not a valid response.")

viable_options_for_investment = ["Investment", "investment", "INVESTMENT"]
viable_options_for_bond = ["Bond", "bond", "BOND"]

if user_decision in viable_options:
 if user_decision in viable_options_for_investment:  # If the user chose INVESTMENT:
    deposit = (int(input("How much money are you depositing? Enter a number: ")))
    interest_rate = int(input("What is the interest rate in percents? Enter a number: "))
    investing_years = int(input("How many years are you planning on investing? "))
    interest = input("Would you like to have 'simple' or 'compound' interest? Enter your answer please: ")

    if interest == "simple": # If the user chose simple interest on investment calculation:
       P = deposit
       r = interest_rate/100
       t = investing_years
       A = P * (1 + r * t)
       output = A
       print(f"The total amount after the interest is applied is {A}")
    elif interest == "compound": # Compound interest on investment calculation
       P = deposit
       r = interest_rate/100
       t = investing_years
       A = P * math.pow((1 + r), t)
       output = A
       print(f"The total amount after the interest is applied is {A}")
 if user_decision in viable_options_for_bond: # If the user chose BOND:
    house_value = int(input("What is the value of your house? "))
    interest_rate = int(input("Enter your interest rate: "))
    repaying_months = int(input("How many months are you planning to take to repay the bond? "))
    P = house_value
    i = interest_rate/100/12
    n = repaying_months
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    output = repayment
    print(f"Each month you will have to repay {repayment}.")
