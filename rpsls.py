# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid Selection"


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return str("rock")
    elif number == 1:
        return str("Spock")
    elif number == 2:
        return str("paper")
    elif number == 3:
        return str("lizard")
    elif number == 4:
        return str("scissors")
    else:
        print "Invalid Integer"
                
            
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
      
    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Select your weapon from the list below"
    print "rock, paper, scissors, lizard, Spock"
    print "======================================"
    print
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    print "Player chooses:", number_to_name(player_number)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
   
    # print out the message for computer's choice
    print "Computer chooses:", comp_choice

    # compute difference of comp_number and player_number modulo five
    diff = (player_number - comp_number) % 5

    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print "Game resulted in a tie!"
    elif diff == 1 or diff == 2:
        print "Player Wins!"
    elif diff == 3 or diff == 4:
        print "Computer Wins!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


