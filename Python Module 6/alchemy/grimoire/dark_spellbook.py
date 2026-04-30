from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients():
	return (["bats", "frogs", "arsenic", "eyeball"])

def dark_spell_record(spell_name: str, ingredients: str):
	validator = validate_ingredients(ingredients)
	if "INVALID" in validator:
		return(f"{spell_name} invalid")
	else:
		return (f"Spell recorded: {spell_name} ({validator})")
		