from functools import partial, reduce, lru_cache, singledispatch
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells == []:
        return 0
    try:
        op = getattr(operator, operation)
        return reduce(op, spells)
    except AttributeError as e:
        print(f"Unsupported operation: {e}")
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchantment = partial(base_enchantment, 50, "fire")
    ice_enchantment = partial(base_enchantment, 50, "ice")
    thunder_enchantment = partial(base_enchantment, 50, "thunder")
    return {"fire": fire_enchantment, "ice": ice_enchantment,
            "thunder": thunder_enchantment}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """
    “Antes de ejecutar la función, compruebo si ya he calculado
    este resultado antes con estos mismos argumentos.”
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


@singledispatch
def spell_dispatcher(arg: Any) -> str:
    """
    singledispatch es un sistema que permite que una función
    cambie su comportamiento según el tipo del argumento que recibe
    """
    return "Unknown spell type"


@spell_dispatcher.register(int)
def int_dispatch(arg: int) -> str:
    return f"Damage spell: {arg} damage"


@spell_dispatcher.register(str)
def str_dispatch(arg: str) -> str:
    return f"Enchantment: {arg}"


@spell_dispatcher.register(list)
def list_dispatch(arg: list) -> str:
    return f"Multi-cast: {len(arg)} spells"


def main() -> None:
    spells = [1, 3, 5]
    x = spell_reducer(spells, "add")
    print(x)


if __name__ == "__main__":
    main()
