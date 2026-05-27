from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy, CreatureError, BattleStrategy)


def battle(opponent1: tuple[CreatureFactory, BattleStrategy],
           opponent2: tuple[CreatureFactory, BattleStrategy]) -> None:
    factory_1, strategy_1 = opponent1
    factory_2, strategy_2 = opponent2
    creature_A = factory_1.create_base()
    creature_B = factory_2.create_base()
    print("* Battle *")
    print(creature_A.describe())
    print(" vs.")
    print(creature_B.describe())
    print(" now fight!")
    try:
        strategy_1.act(creature_A)
        strategy_2.act(creature_B)
    except CreatureError as e:
        print(f"Battle error, aborting tournament: {e}")
    print()


def tournament(opponents: list[tuple[CreatureFactory,
                                     BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            opponent1 = opponents[i]
            opponent2 = opponents[j]
            battle(opponent1, opponent2)


def main() -> None:

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    normal_strategy = NormalStrategy()
    defensive_strategy = DefensiveStrategy()
    aggressive_strategy = AggressiveStrategy()
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    first_opponents = [(flame_factory, normal_strategy),
                       (healing_factory, defensive_strategy)]
    tournament(first_opponents)
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    second_opponents = [(flame_factory, aggressive_strategy),
                        (healing_factory, defensive_strategy)]
    tournament(second_opponents)
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    third_opponents = [(aqua_factory, normal_strategy),
                       (healing_factory, defensive_strategy),
                       (transform_factory, aggressive_strategy)]
    tournament(third_opponents)


if __name__ == "__main__":
    main()
