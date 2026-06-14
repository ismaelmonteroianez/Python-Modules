from typing import Callable


def mage_counter() -> Callable:
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    base_power = initial_power
    def accumulate(amount):
        nonlocal base_power
        base_power+= amount
        return base_power
    return accumulate



def enchantment_factory(enchantment_type: str) -> Callable:
    def weapon(weapon_type: str):
        return f"{enchantment_type} {weapon_type}"
    return weapon


def memory_vault() -> dict[str, Callable]:
    memories = {}
    def store(key, value):
        memories[key] = value
    def recall(key):
        if key not in memories:
            return "Memory not found"
        else:
            return memories[key]
    return {"store":store, "recall":recall}
