import random
from art import logo
import os

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  pick = random.choice(cards)
  return pick

def calculate_score(cards_list):
  if len(cards_list) == 2 and sum(cards_list) == 21:
    return 0
  elif 11 in cards_list and sum(cards_list) > 21:
    cards_list.remove(11)
    cards_list.append(1)
  return sum(cards_list)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  elif user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def blackjack():

  print("Welcome to Blackjack game!")
  print(logo) 
       
  user_cards = []
  computer_cards = []
  game_over = False

  for i in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
  

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Dealer cards: {computer_cards}, current score: {computer_score}")
  
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      q = input("Do you want to draw another card? Enter 'y' for yes, 'n' for no: ")
      if q == "y":
        another_user_pick = deal_card()
        print(f"You picked {another_user_pick}")
        user_cards.append(another_user_pick)
      else:
        game_over = True
        print("Ok, it's dealer's turn.")

  while computer_score != 0 and computer_score < 17:
    another_computer_pick = deal_card()
    print(f"Dealer picked {another_computer_pick}")
    computer_cards.append(another_computer_pick)
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Dealer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  cls = lambda: os.system('cls')
  cls()
  blackjack()