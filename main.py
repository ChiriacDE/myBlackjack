############### Blackjack Project #####################
import random
from art import logo
import os

x = " " #Its prupose is to create spaces
clear = lambda: os.system('cls')

def deal_card():
  """Returns a random card from the main deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Take a list of cards as imput and returns the score"""
  #Check for an 11 (ace). If the score is already over 21, replace the 11 with a 1 
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You  went over. You lose \U0001F44E"

  if user_score == computer_score: #If the computer and user both have the same score, then it's a draw. 
    return "Draw... \U0001F643"
  elif computer_score == 21: #If the computer has a blackjack (0), then the user loses.
    return "Your opponent wins with Blackjack. You lose. \U0001F626"
  elif user_score == 21: #If the user has a blackjack (0), then the user wins.
    return "You win with a Blackjack! \U0001F389 \U0001F973 \U0001F389"
  elif user_score > 21: #If the user_score is over 21, then the user loses.
    return "You  went over. You lose \U0001F44E"
  elif computer_score > 21: #If the computer_score is over 21, then the computer loses.
    return "Your opponent went over. You win \U0001F973"
  else: # If none of the above, then the player with the highest score wins.
    if user_score > computer_score:
      return "You win \U0001F973"
    else:
      return "Your opponent win \U0001F626"


def play_game():
  """Runs the game"""
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False

  #Deal the user and computer 2 cards
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    #Call calculate_score() for users and computers cards
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"{x * 10}Your cards: {user_cards}, current score: {user_score}")
    print(f"{x * 10}Computer's first card: {computer_cards[0]}")

    #Check if the game is there's a Blackjack or if it goes over
    if user_score >= 21:
      game_over = True
    else:
      #Ask for another card
      another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      #Deals another card
      if another_card == "y":
        user_cards.append(deal_card())
      #The game has ended
      elif another_card == "n":
        game_over = True

  #Once the user is done, computer should keep drawing cards as long as it has a score less than 17.
  while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"{x * 10}Your final hand: {user_cards}, final score: {user_score}")
  print(f"{x * 10}Computers final hand: {computer_cards}, final score: {computer_score}")

  #Call compare score function
  print(compare(user_score, computer_score)  )

#Print first of all the rules
print("#################### Our House Rules #########################\n")
print(f"{x * 4}## The deck is unlimited in size.")
print(f"{x * 4}## The deck is unlimited in size.")
print(f"{x * 4}## There are no jokers.")
print(f"{x * 4}## The Jack/Queen/King all count as 10.")
print(f"{x * 4}## The the Ace can count as 11 or 1.")
print(f"{x * 4}## The cards have equal probability of being drawn.")
print(f"{x * 4}## Cards are not removed from the deck as they are drawn.")
print(f"{x * 4}## The computer is the dealer.\n")

#Ask the user if they want to restart the game.
while input("Do you a game of BlackJack? Type 'y' or 'n': ").lower() == "y":
    clear()
    play_game()

