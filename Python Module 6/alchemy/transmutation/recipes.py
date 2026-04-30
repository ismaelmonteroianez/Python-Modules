from ..elements import create_air
from elements import create_fire
from alchemy.potions import strength_potion


def lead_to_gold():
	return(f"Recipe transmuting Lead to Gold: brew {create_air()} and {strength_potion()} mixed with {create_fire()}")
