from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target, power):
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target, power):
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target, power):
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return ("Spell fizzled")
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def casts_spells(target, power):
        spell_list = []
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


def main():
    combined = spell_combiner(fireball, lightning_bolt)
    print(combined("Dragon", 50))


if __name__ == "__main__":
    main()
