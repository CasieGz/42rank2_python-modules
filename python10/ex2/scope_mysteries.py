#!/usr/bin/env python3

from typing import Callable, Any


def mage_counter() -> Callable:
    '''
    Create a counting closure:
    - Return a function that counts how many times it’s been called
    - Each call should return the current count (starting from 1)
    - The counter should persist between calls
    - Creating two separate counters must yield independent state.
    - Use closure to maintain state without global variables
    '''
    counter = 0

    def increment() -> int:
        nonlocal counter
        counter += 1
        return counter

    return increment


def spell_accumulator(initial_power: int) -> Callable:
    '''
    Create power accumulator:
    - Return a function that accumulates power over time
    - Each call adds the given amount to the total power
    - Return the new total power after each addition
    - Start with initial_power as the base
    '''
    power = initial_power

    def increase(increment: int) -> int:
        nonlocal power
        power += increment
        return power

    return increase


def enchantment_factory(enchantment_type: str) -> Callable:
    '''
    Create enchantment functions:
    - Return a function that applies the specified enchantment
    - The returned function takes an item name and
      returns enchanted description
    - Format: "enchantment_type item_name" (e.g., "Flaming Sword")
    - Each factory creates functions with different enchantment types
    '''
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, Callable]:
    '''
    Create a memory management system:
    - Return a dict with ’store’ and ’recall’ functions
    - ’store’ function: takes (key, value) and stores the memory
    - ’recall’ function: takes (key) and returns stored value or
      "Memory not found"
    - Use closure to maintain private memory storage
    '''
    vault: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        vault[key] = value

    def recall(key: Any) -> Any:
        return vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    print(flaming("Sword"))
    frozen = enchantment_factory("Frozen")
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    key = "secret"
    value = 42
    functions = memory_vault()
    store = functions["store"]
    store(key, value)
    print(f"Store '{key}' = {value}")
    recall = functions["recall"]
    print(f"Recall '{key}': {recall(key)}")
    print(f"Recall 'unknown': {recall('unknown')}")
