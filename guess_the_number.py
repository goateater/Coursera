# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#imported modules
import simplegui,math,random

#Global Variables

num_range = 100
secret_number = 0
attempts = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global secret_number
    global attempts
    
    #define the secret number
    secret_number = random.randrange(1,num_range)
    
    # setup the number of attempts per game
    if num_range == 100:
        attempts = 7
    elif num_range == 1000:
        attempts = 10
    print
    print "Welcome to 'Guess The Number!'"
    print "Your game start with", attempts,"guesses, Good Luck!."
    print
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()
    print "Numbers range between 1 and 100, you have", attempts,"guesses."
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()
    print "Numbers range between 1 and 1000, you have", attempts,"guesses."

def input_guess(guess):
    # main game logic goes here
    # convert guess string to integer
    guess = int(guess)
    print
    print "Guess was", guess
    
    # Setup amount of guesses and decrement
    global attempts
    attempts -= 1
    print "You have",attempts,"guesses left" 
    
    # High, Low, Correct, based on guesses for Secret Numver
    if guess == secret_number:
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "You are correct!, Congratulations you win!!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print
        print "Starting a new game"
        new_game()
        return
    elif guess > secret_number:
        print "Lower!"
        print
    elif guess < secret_number:
        print "Higher!"
        print
        
    
    if attempts == 0:
        print "Game Over, Nice Try!"
        new_game()
        return
 
    
# create frame
frame = simplegui.create_frame("Guess The Number",0,200,200)

# register event handlers for control elements and start frame
input = frame.add_input("Enter Guess:",input_guess,75)
button1 = frame.add_button("Range is [0,100)",range100,150)
button2 = frame.add_button("Range is [0,1000)",range1000,150)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
