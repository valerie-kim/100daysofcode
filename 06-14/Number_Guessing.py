#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art2 import logo, congrats, lost
print(logo)

# Select a number to be used for the game
num = random.randint(1,100)
  
def guess_number():
  global i
  while i > 0:
    # Ask the user to enter a number
    user_num = int(input("\nChoose a number betweem 1 and 100: "))
    if user_num > num+20:
      print("Too high")
    elif user_num > num and user_num < num+20:
      print("Slightly high, almost there")
    elif user_num < num-20:
      print("Too low")
    elif user_num < num and user_num > num-20:
      print("Slightly low, almost there")
    elif user_num == num:
      print(f"The number is {num} and you guessed {user_num}.")
      print("Horayyy!! You got it!")
      print(congrats)
      break
    i -= 1
    print(f"You have {i} left chance")
    if i == 0:
      print(f"The number is {num}. Bummer!")
      print(lost)

level = input("'Easy' or 'Hard'? ").title()
if level == "Easy":
  i = 10
  guess_number()
elif level == "Hard":
  i = 5
  guess_number()