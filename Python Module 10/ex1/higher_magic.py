from collections.abc import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return ("Spell fizzled")
    return conditional


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    def casts_spells(target: str, power: int) -> list[str]:
        spell_list: list[str] = []
        for spell in spells:
            spell_list.append(spell(target, power))
        return spell_list
    return casts_spells


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} dealing {power} damage"


def lightning_bolt(target: str, power: int) -> str:
    return f"Lightning strikes {target} dealing {power} damage"


def enough_power(_target: str, power: int) -> bool:
    if power >= 20:
        return True
    else:
        return False


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon', 50)[0]}, "
          f"{combined('Dragon', 50)[1]}")
    print()
    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}, "
          f"Amplified: {amplified('Dragon', 10)}")
    print()
    print("Testing conditional caster...")
    conditional = conditional_caster(enough_power, lightning_bolt)
    print(conditional("Mage", 25))
    print()
    print(conditional("Mage", 10))
    print()
    print("Testing spell sequence...")
    spell_barrage = spell_sequence([fireball, lightning_bolt, heal])
    spell_list = spell_barrage("Zombie", 40)
    for spell in spell_list:
        print(spell)


if __name__ == "__main__":
    main()
