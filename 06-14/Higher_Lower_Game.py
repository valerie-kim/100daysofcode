######## MY VERSION ########
from art3 import logo, vs
from game_data import data
from random import randint
import os
cls = lambda: os.system('cls')

i=0
end = False
while not end:
  print(logo)
  random_numA = randint(0,len(data)-1)
  random_numB = randint(0,len(data)-1)

  A = data[random_numA]
  name = data[random_numA]['name']
  description = data[random_numA]['description']
  country = data[random_numA]['country']
  B = data[random_numB]
  name2 = data[random_numB]['name']
  description2 = data[random_numB]['description']
  country2 = data[random_numB]['country']
  
  print("Current score:", i)
  print(f"\nCompare A: {name}, {description}, {country}")
  print(vs)
  print(f"Against B: {name2}, {description2}, {country2}")

  follower = input("\nWho has more followers? A or B? ").lower()

  if follower == 'b':
    if A['follower_count'] > B['follower_count']:
      print("Sorry, you are wrong")
      q = input("\nDo you want to start over? enter 'y' for yes, 'n' for no: ").lower()
      if q == 'n':
        end = True
      else:
        cls()
    else:
      print("Congrats! Next round")
      i += 1
      cls()
  elif follower == 'a':
    if A['follower_count'] > B['follower_count']:
      print("Congrats! Next round")
      i += 1
      cls()
    else:
      print("Sorry, you are wrong")
      q = input("\nDo you want to start over? enter 'y' for yes, 'n' for no: ")
      if q == 'n':
        end = True
      else:
        cls()
  else:
    print("You entered wrong.")


##### Refactored #####

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()
    
    print("Current score:", score)
    print(f"\nCompare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("\nWho has more followers? A or B? ").lower()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    cls()
    print(logo)
    if is_correct:
      score += 1
      print("Congrats! Next round")
    else:
      print("Sorry, you are wrong")
      game_continue = False

game()


