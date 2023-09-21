from data import data
import random
from replit import clear

"""
from data randomly get 2 data
choose 1 or 2 
if 1 is greater than 2 and 1 chosen stay game continues and shuffles another hasło
if 2 chosen and its greater than 1, 2 replaces 1 and shuffles another hasło
if wrong answer game stops
"""


def data_format(person):
    person_name = person["name"]
    person_description = person["description"]
    person_country = person["country"]
    return f"{person_name}, {person_description}, from {person_country}"


def check_answer(player_choice, a_followers, b_followers):
    if a_followers > b_followers:
        return player_choice == "A"
    else:
        return player_choice == "B"


players_points = 0
second_person = random.choice(data)
while True:
    first_person = second_person
    if first_person == second_person:
        second_person = random.choice(data)
    print("A:", data_format(first_person))
    print("\nAgainst\n")
    print("B:", data_format(second_person))

    a_followers = first_person["follower_count"]
    b_followers = second_person["follower_count"]

    player_choice = input(
        "Choose which person has more followers in your opinion: "
    ).upper()

    clear()

    if is_correct := check_answer(player_choice, a_followers, b_followers):
        players_points += 1
        print("You're right")
    else:
        print("You're wrong")
        print(f"Your points: {players_points}")
        break
    print(f"Your points: {players_points}")
