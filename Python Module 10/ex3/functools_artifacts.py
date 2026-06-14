import functools
import operator
from typing import Callable

def spell_reducer(spells: list[int], operation: str) -> int:
    if spells == []:
        return 0 
    try:
        op = getattr(operator, operation)
        return functools.reduce(op, spells)
    except AttributeError as e:
        print(f"Unsupported operation: {e}")
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    functools.partial(base_enchantment)

def main():
    spells = [1,3,5]
    x = spell_reducer(spells, "add")
    print(x)

main()
