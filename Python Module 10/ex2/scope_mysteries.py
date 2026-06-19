from collections.abc import Callable


def mage_counter() -> Callable:
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    new_power = initial_power

    def accumulate(amount):
        nonlocal new_power
        new_power += amount
        return new_power
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
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    base_power = 100
    accumulate = spell_accumulator(base_power)
    amount = 20
    print(f"Base: {base_power}, add {amount}: {accumulate(amount)}")
    amount = 30
    print(f"Base: {base_power}, add {amount}: {accumulate(amount)}")
    print()
    print("Testing enchantment factory...")
    flaming_sword = enchantment_factory("Flaming")
    print(flaming_sword("Sword"))
    frozen_shield = enchantment_factory("Frozen")
    print(frozen_shield("Shield"))
    print()
    print("Testing memory vault...")
    vault = memory_vault()
    store = vault["store"]
    recall = vault["recall"]
    store("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")


if __name__ == "__main__":
    main()
