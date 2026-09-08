#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list[int] = []  # syntax to create a list. "list[int]" is
    # the type hint. the "[]" is actually creating an empty list
    for item in sys.argv[1:]:
        try:
            scores += [int(item)]  # appends elem. at end of list
        except ValueError:
            print(f"Invalid parameter: '{item}'")
    if not scores:  # checks if the list is empty
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
