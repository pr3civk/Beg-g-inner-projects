import random

# create a deck of cards
deck = []
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = {'ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10}

for suit in suits:
    for value in values:
        deck.append(value + ' of ' + suit)

# function to calculate the total points of a hand
def calculate_hand(hand):
    total = 0
    num_aces = 0
    for card in hand:
        value = card.split()[0]
        if value == 'ace':
            num_aces += 1
        total += values[value]
    while num_aces > 0 and total > 21:
        total -= 10
        num_aces -= 1
    return total

# deal two cards to the player and two to the dealer
player_hand = [deck.pop(random.randint(0, len(deck)-1)), deck.pop(random.randint(0, len(deck)-1))]
dealer_hand = [deck.pop(random.randint(0, len(deck)-1)), deck.pop(random.randint(0, len(deck)-1))]

# game loop
while True:
    print('Your hand:', player_hand)
    print('Dealer showing:', dealer_hand[0])
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    if player_total == 21:
        print('Blackjack! You win.')
        break
    elif player_total > 21:
        print('Bust. You lose.')
        break
    else:
        choice = input('Hit or stand? ')
        if choice.lower() == 'hit':
            player_hand.append(deck.pop(random.randint(0, len(deck)-1)))
        elif choice.lower() == 'stand':
            while dealer_total < 17:
                dealer_hand.append(deck.pop(random.randint(0, len(deck)-1)))
                dealer_total = calculate_hand(dealer_hand)
            if dealer_total > 21:
                print('Dealer bust. You win.')
            elif dealer_total > player_total:
                print('Dealer wins.')
            elif dealer_total < player_total:
                print('You win.')
            else:
                print('Push.')
            break
