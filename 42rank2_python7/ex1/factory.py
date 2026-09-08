from ex0.factory import CreatureFactory
from . import creatures


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures.Sproutling:
        return creatures.Sproutling()

    def create_evolved(self) -> creatures.Bloomelle:
        return creatures.Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures.Shiftling:
        return creatures.Shiftling()

    def create_evolved(self) -> creatures.Morphagon:
        return creatures.Morphagon()
