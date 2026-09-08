#!/usr/bin/env python3

import random

ALL_ACHIEVEMENTS = ["Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme", "Untouchable", "Sharp Mind",
                    "Boss Slayer"]


def gen_player_achievements() -> set[str]:
    count = len(ALL_ACHIEVEMENTS)
    # randint() method returns an integer number selected
    # element from the specified range. (start, stop+1)
    num_achievements = random.randint(count//3, (2*count)//3)
    # calculating reasonale amount of achievements (// is division rounded to
    # an integer, with just / we get float) with count 13 it will be 4 - 8

    # sample() returns a list with a specified number of
    # randomly selected items from a sequence.
    player_achievements = (random.sample(ALL_ACHIEVEMENTS, k=num_achievements))
    return set(player_achievements)  # set() creates a set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    print(f"Player Alice: = {alice}")
    bob = gen_player_achievements()
    print(f"Player Bob: = {bob}")
    charlie = gen_player_achievements()
    print(f"Player Charlie: = {charlie}")
    dylan = gen_player_achievements()
    print(f"Player Dylan = {dylan}\n")

    # union() returns a set that contains all items from the original set,
    # and all items from the specified set(s).
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}\n")

    # intersection() returns a set that contains the similarity between
    # two or more sets.
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")

    # difference() returns a set that contains the difference between
    # two or multiple sets to the first one.
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")

    all_achievements = set(ALL_ACHIEVEMENTS)
    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")
