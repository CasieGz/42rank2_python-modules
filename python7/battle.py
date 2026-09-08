#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:

    base_creature_1 = factory1.create_base()
    base_creature_2 = factory2.create_base()

    print("Testing battle")
    print(base_creature_1.describe())
    print("vs.")
    print(base_creature_2.describe())
    print("fight!")
    print(base_creature_1.attack())
    print(base_creature_2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    testing_factory(flame_factory)

    print()
    aqua_factory = AquaFactory()
    testing_factory(aqua_factory)

    print()
    test_fight(flame_factory, aqua_factory)
