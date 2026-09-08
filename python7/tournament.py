#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, \
    DefensiveStrategy, InvalidStrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            opponent_a = factory_a.create_base()
            opponent_b = factory_b.create_base()

            print("\n* Battle *")
            print(opponent_a.describe())
            print("vs.")
            print(opponent_b.describe())
            print("now fight!")

            try:
                print(strategy_a.act(opponent_a))
                print(strategy_b.act(opponent_b))

            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    # Tournament 0
    print("Tournament 0 (basic)")
    battle_0: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ]
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(battle_0)

    # Tournament 1
    print("\nTournament 1 (error)")
    battle_1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ]
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(battle_1)

    # Tournament 2
    print("\nTournament 2 (multiple)")
    battle_2: list[tuple[CreatureFactory, BattleStrategy]] = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
        ]
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(battle_2)
