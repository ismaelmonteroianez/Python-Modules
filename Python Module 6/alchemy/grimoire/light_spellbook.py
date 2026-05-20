from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return (["earth", "air", "fire", "water"])


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validator = validate_ingredients(ingredients)
    if "INVALID" in validator:
        return (f"{spell_name} invalid")
    else:
        return (f"Spell recorded: {spell_name} ({validator})")
