from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class InvalidStrategyError(Exception):
    def __init__(
            self,
            creature_name: str | None = None,
            strategy_name: str | None = None
            ) -> None:

        if creature_name is None or strategy_name is None:
            message: str = "Unknown Strategy Error"

        else:
            message = f"Invalid Creature '{creature_name}' " \
                f"for this {strategy_name}"

        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """returns a bool indicating that a Creature is suitable
        for the strategy"""
        pass

    def _strategy_name(self) -> str:
        return self.__class__.__name__. \
                replace("Strategy", " Strategy").lower()


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, self._strategy_name())
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(creature.name, self._strategy_name())
        else:
            return "\n".join([
                creature.transform(),
                creature.attack(),
                creature.revert()
                ])


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(creature.name, self._strategy_name())
        else:
            return "\n".join([creature.attack(), creature.heal()])
