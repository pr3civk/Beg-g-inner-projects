import random
from replit import clear

deck = []
cards = { "A" : 11, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
          "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10}
suits = ["♥ Hearts", "♦ Diamonds", "♣ Clubs", "♠ Spades"]

for card_name in cards:
    for suit in suits:
        full_card_name = (card_name + " of " + suit)
        deck.append(full_card_name)

random.shuffle(deck)

def cards_in_hand_value(hand):
    total_value = 0
    for card in hand:
        card_value = card.split()[0]
        total_value += cards[card_value]
    return(total_value)

player_hand = [deck.pop(0), deck.pop(2)]
dealer_hand = [deck.pop(1), ]

#Game:
print(f"Players' hand: {player_hand}, Points: {cards_in_hand_value(player_hand)}")
print(f"Dealers' hand: [{dealer_hand[0]}, 'x' ], Points: {cards_in_hand_value(dealer_hand)}")
game_continue = True
while game_continue:
    if cards_in_hand_value(player_hand) < 21 and cards_in_hand_value(dealer_hand) < 21:
        players_choice = input("Do you want to hit or stand?: ").lower()
        if players_choice == "hit":
            deck.pop(3)
            player_hand.append(deck.pop(3))
            print(f"Players' hand: {player_hand}, Points: {cards_in_hand_value(player_hand)}")
            continue
        elif players_choice == "stand":
            deck.pop(4)
            dealer_hand.append(deck.pop(4))
            print(f"Dealers' hand: {dealer_hand}, Points: {cards_in_hand_value(dealer_hand)}")
            if cards_in_hand_value(dealer_hand) < 17 and cards_in_hand_value(player_hand) > cards_in_hand_value(dealer_hand):
                deck.pop(5)
                dealer_hand.append(deck.pop(5))
                print(f"Players' hand: {player_hand}, Points: {cards_in_hand_value(player_hand)}")
                print(f"Dealers' hand: {dealer_hand}, Points: {cards_in_hand_value(dealer_hand)}")
            elif cards_in_hand_value(dealer_hand) > 17:
                print(f"Players' hand: {player_hand}, Points: {cards_in_hand_value(player_hand)}")
                print(f"Dealers' hand: {dealer_hand}, Points: {cards_in_hand_value(dealer_hand)}")
    if cards_in_hand_value(player_hand) > 21:
        print("Bust! You've lost!")
    elif cards_in_hand_value(player_hand) == 21:
        print("Blackjack! You've won!")
    elif cards_in_hand_value(dealer_hand) > 21:
        print("You've won!")
    elif cards_in_hand_value(dealer_hand) == 21:
        print("You've lost!")
    elif cards_in_hand_value(player_hand) > cards_in_hand_value(dealer_hand):
        print("You've won!")
    elif cards_in_hand_value(player_hand) < cards_in_hand_value(dealer_hand):
        print("You've lost!")
    elif cards_in_hand_value(player_hand) == cards_in_hand_value(dealer_hand):
        print("Draw! You've collected the same amount of points!")
    game_continue = input("Do you want to start again? y if yes, n if no:  ").lower()
    if game_continue == "y":
        clear()
    elif game_continue == "n":
        game_continue = False
        print("Thank you for playing!")
