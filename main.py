import time 
import random
'''
we are gonna play the guessing game 
There's a secret number (from 1 to 100), and the user needs to 
guess the secret number
if the user's guess is correct, the user win the game
else they lose the game 
'''

'''
we are gonna play the guessing game 
There's a secret number (from 1 to 100), and the user needs to 
guess the secret number
if the user's guess is correct, the user win the game
else they lose the game 
'''

# STEP1: print out the welcome message and let the user know the game rules

print("⭐️ ⭐️ Welcome to my game called guessing game, this is made by me cool guy Jonathan")
time.sleep(1)
print("\nThe rules are that there is a number from 1 to 100 that you have to guess")
time.sleep(1)
print("\nYou only have six trys if you don't get it on your all six trys you lose the game but if you get the number you win.")
time.sleep(1)
print("\nGood luck on your journey to finding the number.")
time.sleep(1)
# STEP 2: ask users for their name
# create a variable called 'name' and assign it to the user's name
# food =  input("enter your username here: ")
Username = input("\nEnter you Username here: ")
time.sleep(1)
# STEP 3: greeting the user by using the Username (e.g. "Hi! Emily. Are you ready? Let's get started!)
print("\nHi! " + Username + " Are you ready? Let's get started!")

# STEP 4: create a variable called "secretNumber" and assign it to 
# a random number from 1 to 100 by using random.randint(start, end)
# but before that you need to import random 
# randomNumber = random.randint(1, 10)

secretNumber = random.randint(1, 100)
# print(f"secretNumber = {secretNumber}")

# STEP 5:  create a boolean variable called 'isCorrectGuess' and assign False to it
# isItGood = False # boolean 
isCorrectGuess = False 

# STEP 6: create a variable "totalGuess" and assign it to how many times the user can guess
totalGuess = 6

# STEP 7: create a while loop to keep asking the user's guesses until they ran out of guesses OR they guess correctly
isCorrectGuess = False 
# not False = True 
# not True = False
# True and False = False 

# STEP 9: using if-else statement to check if the user's guess is correct or not
while totalGuess > 0 and not isCorrectGuess:
  
  # STEP 8: get user guess and convert it into integer data type and assign it to the userGuess variable 
  # num = int(input("Enter a number:"))
  Guessnumber = int(input("\nEnter your Guess: "))
  if Guessnumber == secretNumber:
    print("Congrats you win the game")
    isCorrectGuess = True 
  else:
    # when the user cannot guess the number
    print("Try again it is not the number")
    # if the guess is wrong, then decrease the totalGuess by 1
    totalGuess = totalGuess - 1
    # TODO: let the user know if their guess number is bigger than the secret number
    # or it's smaller than the secret number
    # show the user how many guesses they have left
    print("you have " + str(totalGuess) + " guesses left")
    time.sleep(1)
    if Guessnumber > secretNumber:
      print("\nYour guess is too high")
    elif Guessnumber < secretNumber:
      print("\nYour guess is too low")
      
# after the loop ends, if the totalGuess is equal to 0 if
if isCorrectGuess == False:
  print("You lose the game, The anwser is " + str(secretNumber))

# TODO: let the users know the secret number at the end of the game 