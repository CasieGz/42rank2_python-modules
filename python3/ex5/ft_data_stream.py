#!/usr/bin/env python3

import random
import typing

PLAYERS = ["alice", "bob", "dylan", "charlie"]
ACTIONS = ["run", "eat", "sleep", "grab", "run", "move", "climb", "swim",
           "release", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        chosen_player = random.choice(PLAYERS)
        chosen_action = random.choice(ACTIONS)
        yield (chosen_player, chosen_action)


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        random_index = random.randint(0, len(events) - 1)
        picked_event = events[random_index]
        # slicing assignment to remove random_index until
        # but excluding random_index + 1
        events[random_index:random_index + 1] = []
        yield picked_event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event = gen_event()
    for i in range(1000):
        player, move = next(event)
        print(f"Event {i}: Player {player} did action {move}")
    event_list = [next(event) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")
    for item in consume_event(event_list):  # here the first call to function
        # also creates generator object and after the for loop
        # takes care of the next() everytime it loops
        print(f"Got event from list: {item}")
        print(f"Remains in list: {event_list}")
