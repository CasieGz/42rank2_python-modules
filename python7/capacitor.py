#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    healing_creature_factory = HealingCreatureFactory()

    print("base:")
    base_healing_creature = healing_creature_factory.create_base()
    print(base_healing_creature.describe())
    print(base_healing_creature.attack())
    print(base_healing_creature.heal())

    print("evolved:")
    evolved_healing_creature = healing_creature_factory.create_evolved()
    print(evolved_healing_creature.describe())
    print(evolved_healing_creature.attack())
    print(evolved_healing_creature.heal())

    print("\nTesting Creature with transform capability")
    transform_creature_factory = TransformCreatureFactory()
    print("base:")
    base_transform_creature = transform_creature_factory.create_base()
    print(base_transform_creature.describe())
    print(base_transform_creature.attack())
    print(base_transform_creature.transform())
    print(base_transform_creature.attack())
    print(base_transform_creature.revert())

    print("evolved:")
    evolved_transform_creature = transform_creature_factory.create_evolved()
    print(evolved_transform_creature.describe())
    print(evolved_transform_creature.attack())
    print(evolved_transform_creature.transform())
    print(evolved_transform_creature.attack())
    print(evolved_transform_creature.revert())
