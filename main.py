import random
from art import logo 
from replit import clear

def blackjack():
  clear()
  print(logo) 
  print("Welcome to Blackjack!")
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  dealer_card = []
  dealer_card.append(random.choice(cards))
  player_card = []
  
  for i in range(0,2):
    player_card.append(random.choice(cards))
  print(f"  Your cards: {player_card}   Your current score = {sum(player_card)}")
  print(f"  Dealer's first card: {dealer_card}")
  
  stop_game = False
  while stop_game == False and sum(player_card) != 21 and sum(player_card) < 21:
    get_a_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_a_card == 'y':
      new_card = random.choice(cards)
      if new_card == 11 and sum(player_card)+11 > 21:
        player_card.append(1)
      else:
        player_card.append(new_card)
      print(f"  Your cards: {player_card}  Current score = {sum(player_card)}")
      print(f"  Dealer's first card: {dealer_card}")
    else:
      stop_game = True
      
  print(f"  Your final Hand: {player_card}  Your final score = {sum(player_card)}")
  
  while sum(dealer_card) != 21 and sum(dealer_card) < 17:
    new_card = random.choice(cards)
    if new_card == 11 and sum(dealer_card)+11 > 21:
      dealer_card.append(1)
    else:
      dealer_card.append(new_card)  
      
  print(f"  Dealer's final hand: {dealer_card}  Dealer's final score:{sum(dealer_card)}")
  
  if sum(player_card) == sum(dealer_card):
    print("It's a tie!")
  elif sum(player_card) > 21:
    print("You went over. You lose!")
  elif sum(dealer_card) > 21:
    print("Dealer went over. You win!")
  elif sum(player_card) > sum(dealer_card):
    print("You win!")
  else:
    print("Dealer wins!")
  replay = input("\nDo you want to play again? Type 'y' or 'n': ")
  if replay == 'y':
    blackjack()

blackjack()



