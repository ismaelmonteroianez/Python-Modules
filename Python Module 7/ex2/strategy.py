from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.transform import TransformCapability
from ex1.healing import HealCapability
from typing import Any


class CreatureError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        temp: Any = creature
        if self.is_valid(creature) is False:
            raise CreatureError(f"Invalid Creature {creature.name}"
                                "for this aggressive strategy")
        print(temp.transform())
        print(temp.attack())
        print(temp.revert())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        temp: Any = creature
        if self.is_valid(creature) is False:
            raise CreatureError(f"Invalid Creature {creature.name}"
                                "for this defensive strategy")
        print(temp.attack())
        print(temp.heal())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
