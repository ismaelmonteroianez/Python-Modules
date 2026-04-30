from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
	allowed_ingredientes = dark_spell_allowed_ingredients()
	for ingredient in ingredients.lower().split():
		if ingredient in allowed_ingredientes:
			return(f"{ingredients} - VALID")
	return(f"{ingredients} - INVALID")