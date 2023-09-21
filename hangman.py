import random as rd


class Hangman:
    def __init__(self):
        self.lives = 10

    def choose_word(self, list):
        return rd.choice(list)

    def hide_word(self, word):
        return [" - "] * len(word)

    def check_the_guess(self, guess, guessing_word, hidden_word):
        for position in range(len(guessing_word)):
            letter = guessing_word[position]
            if letter == guess:
                hidden_word[position] = guess

    def is_win(self, hidden_word):
        if " - " not in hidden_word:
            print(hidden_word)
            return True

    def is_lost(self, guess, guessing_word):
        if guess not in guessing_word and self.lives > 0:
            self.lives -= 1
        return self.lives


h = Hangman()
list_of_words = [
   
]

chosen_word = h.choose_word(list_of_words)
hidden_word = h.hide_word(chosen_word)
while True:
    print(hidden_word)
    print("lives: ", h.lives)
    players_guess = input("Guess a word: ")
    h.check_the_guess(players_guess, chosen_word, hidden_word)
    if h.is_win(hidden_word):
        print("You've won!")
        break

    elif h.lives == 1:
        print("You've lost!")
        break
    else:
        h.is_lost(players_guess, chosen_word)
