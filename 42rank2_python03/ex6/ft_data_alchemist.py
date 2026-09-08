#!/usr/bin/env python3

import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                          "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    capitalize_players = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalize_players}")

    only_capitalized_players = [name for name in players
                                if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized_players}\n")

    players_dict = {name: random.randint(0, 1000)
                    for name in capitalize_players}
    print(f"Score dict: {players_dict}")

    score_average = round(sum(players_dict.values()) / len(players_dict), 2)
    print(f"Score average is {score_average}")

    high_scores = {name: players_dict[name] for name in players_dict
                   if players_dict[name] > score_average}
    print(f"High scores: {high_scores}")
