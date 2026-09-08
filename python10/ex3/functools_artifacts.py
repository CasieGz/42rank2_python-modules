#!/usr/bin/env python3

from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    '''
    Reduce spell powers:
    - Use functools.reduce to combine all spell powers
    - Support operations: "add", "multiply", "max", "min"
    - Use operator module functions (add, mul, etc.)
    - Return the final reduced value
    - If spells is empty, return 0
    - If operation is unknown, properly handle the error
    '''
    function_dict: dict = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if not spells:
        return 0
    chosen_func = function_dict.get(operation)
    if not chosen_func:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(chosen_func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    '''
    Create partial applications:
    - Take a base enchantment function with signature
    (power: int, element: str, target: str) -> str
    - Use functools.partial to create 3 specialized versions
    - Each version pre-filling power=50 and the element

    Partial functions in Python is a function that is created by fixing
    a certain number of arguments of another function.
    '''
    return {
        "water": partial(base_enchantment, 50, "Water"),
        "fire": partial(base_enchantment, 50, "Fire"),
        "earth": partial(base_enchantment, 50, "Earth"),
    }


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    '''
    Cached fibonacci:
    - Use functools.lru_cache decorator for memoization
    - Implement fibonacci sequence calculation
    - Function should return the nth Fibonacci number
    - The cache should improve performance for repeated calls
    - Return the nth fibonacci number
    '''
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1))


def spell_dispatcher() -> Callable[[Any], str]:
    '''
    Create single dispatch system:
    - Use decorator functools.singledispatch to create a spell system
    - The base function receives Any and handles unknown spell type
    - Handle different types: int (damage spell), str (enchantment),
    list (multi-cast)
    - Return the dispatcher function
    - Each type should have appropriate spell behavior
    '''
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Casting {spell} enchantment!"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells: {', '.join(s for s in spell)}"

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} with {element} Enchantment (Level {power})"


if __name__ == "__main__":
    print("Testing spell reducer...")
    test_spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(test_spells, 'add')}")
    print(f"Product: {spell_reducer(test_spells, 'multiply')}")
    print(f"Max: {spell_reducer(test_spells, 'max')}")

    print("\nTesting partial enchanter...")
    functions = partial_enchanter(base_enchantment)
    for func in functions.values():
        print(func("Casie"))

    print("\nTesting memoized fibonacci...")
    test_nbrs = [0, 1, 10, 15]
    for nbr in test_nbrs:
        print(f"Fib({nbr}): {memoized_fibonacci(nbr)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(f"Damage spell: {spell(42)}")
    print(f"Enchantment: {spell('fireball')}")
    spell_list = ["wipe", "get up", "wash hands", "leave"]
    print(f"Multi-cast: {spell(spell_list)}")
    print(f"Unknown type: {spell(8.0)}")
