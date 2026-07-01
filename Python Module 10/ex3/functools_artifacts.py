from functools import partial, reduce, lru_cache, singledispatch
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    `reduce` repeatedly applies the selected operation to combine
    all values in the list into a single result.
    """
    if not spells:
        return 0
    if operation == "add":
        op = operator.add
    elif operation == "multiply":
        op = operator.mul
    elif operation == "max":
        op = max
    elif operation == "min":
        op = min
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(op, spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable[[str], str]]:
    """
    `partial` creates specialized versions of a function by
    pre-filling some of its arguments while leaving the remaining
    ones to be provided later.
    """
    fire_enchantment = partial(base_enchantment, 50, "fire")
    ice_enchantment = partial(base_enchantment, 50, "ice")
    thunder_enchantment = partial(base_enchantment, 50, "thunder")
    return {"fire": fire_enchantment, "ice": ice_enchantment,
            "thunder": thunder_enchantment}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """
    Before executing the function, `lru_cache` checks whether it
    has already calculated the result for the same arguments."
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(_: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatch.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatch.register(list)
    def _(arg: list[Any]) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment with power {power} on {target}"


def main() -> None:
    print("Testing spell reducer...")
    spells = [30, 40, 30]
    sum_test = spell_reducer(spells, "add")
    print(f"Sum: {sum_test}")
    product_test = spell_reducer(spells, "multiply")
    print(f"Product: {product_test}")
    max_test = spell_reducer(spells, "max")
    print(f"Max: {max_test}")
    print()
    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"]("dragon"))
    print(enchantments["ice"]("goblin"))
    print(enchantments["thunder"]("wizard"))
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "ice ray", "lightning bolt"]))
    print(dispatcher(42.42))


if __name__ == "__main__":
    main()
