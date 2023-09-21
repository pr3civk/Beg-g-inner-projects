import random


class Deck:
    def __name__(self):
        print(
            f"Players' hand {player_hand} : {deck.count_points(player_hand)} ",
            "\n",
            f"Dealers' hand {dealer_hand} : {deck.count_points(dealer_hand)} ",
        )

    def deck(self):
        self.cards = {
            "A": 11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
        }
        self.suits = ["♥ Hearts", "♦ Diamonds", "♣ Clubs", "♠ Spades"]
        return [(card, suit) for card in self.cards for suit in self.suits]

    def shuffle_deck(self, deck):
        return random.shuffle(deck)

    def count_points(self, hand, total=0):
        for card in hand:
            for card_value in card:
                if card_value in deck.cards:
                    if card_value == "A" and total > 10:
                        ace_value = 1
                        total += ace_value
                    else:
                        value = deck.cards[card_value]
                        total += value

        return total


class Player(Deck):
    def __init__(self):
        super().deck()

    def add_card(self, deck, hand):
        withdraw_card = deck.pop(0)
        hand.append(withdraw_card)


class Result(Deck):
    def result(self, pl_points, dl_points):
        if (
            pl_points > dl_points
            and pl_points <= 21
            or pl_points <= dl_points
            and dl_points > 21
        ):
            return f"Player won with {pl_points} in hand"
        elif pl_points < dl_points <= 21 or pl_points > 21:
            return f"Player lost with dealers' points {dl_points} in hand"
        elif pl_points == dl_points:
            return f"Draw with {pl_points} in hand"


deck = Deck()
player = Player()
dealer = Player()
result = Result()

card_deck = deck.deck()
deck.shuffle_deck(card_deck)
game_on = True
player_game = True
dealer_game = True

while game_on:
    player_hand = []
    dealer_hand = []
    for _ in range(2):
        player.add_card(card_deck, player_hand)
    dealer.add_card(card_deck, dealer_hand)
    while player_game:
        deck.__name__()
        if deck.count_points(player_hand) == 21:
            result.result(
                deck.count_points(player_hand),
                deck.count_points(dealer_hand),
            )
            player_game = False
            dealer_game = False
        else:
            player_decision = input(
                "Would you like to withdraw another card or stay? y/n: "
            )
            if player_decision in ["yes", "y"]:
                player.add_card(card_deck, player_hand)
                result.result(
                    deck.count_points(player_hand),
                    deck.count_points(dealer_hand),
                )
                if deck.count_points(player_hand) > 21:
                    dealer.add_card(card_deck, dealer_hand)
                    deck.__name__()
                    player_game = False
                    dealer_game = False
            elif player_decision in ["no", "n"]:
                dealer.add_card(card_deck, dealer_hand)
                player_game = False

    while dealer_game:
        deck.__name__()
        if deck.count_points(dealer_hand) <= 17 and deck.count_points(
            dealer_hand
        ) < deck.count_points(player_hand):
            dealer.add_card(card_deck, dealer_hand)
        else:
            dealer_game = False
    print(
        result.result(
            deck.count_points(player_hand),
            deck.count_points(dealer_hand),
        )
    )
    game_over = input("Do you want to play again? y/n: ")
    if game_over in ["yes", "y"]:
        card_deck = deck.deck()
        deck.shuffle_deck(card_deck)
        player_game = True
        dealer_game = True
        continue
    else:
        game_on = False
        print("Thank You for the game!")
