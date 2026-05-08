from ex0 import FlameFactory, AquaFactory, CreatureFactory


def validate_creature(factory: CreatureFactory) -> None:
    print("Testing factory")
    creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def fight(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    print("Testing battle")
    fire_creature = factory_1.create_base()
    water_creature = factory_2.create_base()
    print(fire_creature.describe())
    print(" vs.")
    print(water_creature.describe())
    print(" fight!")
    print(fire_creature.attack())
    print(water_creature.attack())


def main() -> None:
    flame_factory = FlameFactory()
    validate_creature(flame_factory)
    print()
    aqua_factory = AquaFactory()
    validate_creature(aqua_factory)
    print()
    fight(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
