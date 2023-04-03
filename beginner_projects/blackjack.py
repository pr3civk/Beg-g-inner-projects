import random

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
         "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
suits = ["♥ Hearts", "♦ Diamonds", "♣ Clubs", "♠ Spades"]

deck = []
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
        if cards["A"] in cards and total_value > 21:
            cards["A"] == 1
    return (total_value)


player_hand = []
dealer_hand = []

is_game_over = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while is_game_over:
    if cards_in_hand_value(player_hand) == 0:
        player_hand = [deck.pop(0), deck.pop(2)]
        dealer_hand = [deck.pop(1), ]
    print(
        f"Players' hand: {player_hand}, Points: {cards_in_hand_value(player_hand)}")
    print(
        f"Dealers' hand: [{dealer_hand[0]}, 'x' ], Points: {cards_in_hand_value(dealer_hand)}")
    if cards_in_hand_value(player_hand) < 21 and cards_in_hand_value(dealer_hand) <= 17:
        players_choice = input("Do you want to hit or stand?: ").lower()
        if players_choice == "hit" or players_choice == "h":
            deck.pop(3)
            player_hand.append(deck.pop(3))
            continue
        elif players_choice == "stand" or players_choice == "s":
            deck.pop(3)
            dealer_hand.append(deck.pop(3))
            if cards_in_hand_value(dealer_hand) < 17 and cards_in_hand_value(player_hand) > cards_in_hand_value(dealer_hand):
                deck.pop(4)
                dealer_hand.append(deck.pop(4))
                print(f"Dealers' hand: [{dealer_hand[0]}, 'x' ], Points: {cards_in_hand_value(dealer_hand)}")
            else:
                print(f"Dealers' hand: [{dealer_hand[0]}, 'x' ], Points: {cards_in_hand_value(dealer_hand)}")
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
    break

is_game_over = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if is_game_over == "y":
    for card in player_hand:
        deck.extend(player_hand[0])
    for card in dealer_hand:
        deck.extend(dealer_hand[0])
    random.shuffle(deck)
    print(deck)

elif is_game_over == "n":
    is_game_over = False
