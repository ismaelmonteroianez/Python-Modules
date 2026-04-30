def validate_ingredients(ingredients: str):
	from .light_spellbook import light_spell_allowed_ingredients
	allowed_ingredientes = light_spell_allowed_ingredients()
	for ingredient in ingredients.lower().split():
		if ingredient in allowed_ingredientes:
			return(f"{ingredients} - VALID")
	return(f"{ingredients} - INVALID")
