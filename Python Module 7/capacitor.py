from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()
    print(" base:")
    healing_creature = healing_factory.create_base()
    print(healing_creature.describe())
    print(healing_creature.attack())
    print(healing_creature.heal())
    print(" evolved:")
    evolved_healing_creature = healing_factory.create_evolved()
    print(evolved_healing_creature.describe())
    print(evolved_healing_creature.attack())
    print(evolved_healing_creature.heal())
    print()
    print("Testing Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    print(" base:")
    transforming_creature = transform_factory.create_base()
    print(transforming_creature.describe())
    print(transforming_creature.attack())
    print(transforming_creature.transform())
    print(transforming_creature.attack())
    print(transforming_creature.revert())
    print(" evolved:")
    evolved_transforming_creature = transform_factory.create_evolved()
    print(evolved_transforming_creature.describe())
    print(evolved_transforming_creature.attack())
    print(evolved_transforming_creature.transform())
    print(evolved_transforming_creature.attack())
    print(evolved_transforming_creature.revert())


if __name__ == "__main__":
    main()
