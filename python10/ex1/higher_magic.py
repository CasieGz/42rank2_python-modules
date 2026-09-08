#!/usr/bin/env python3

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    '''
    Combine two spells:
    - Return a new function that calls both spells with the same arguments
    - The combined spell should return a tuple of both results
    - Example: combined = spell_combiner(fireball, heal)
    '''
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    '''
    Amplify spell power:
    - Returns a function with the same signature as the original spell
    - Returns a new spell where the power is multiplied before casting.
    - Example: mega_fireball = power_amplifier(fireball, 3)
    '''
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    '''
    Cast spell conditionally:
    - Returns a new spell that only casts if a condition is True.
    - If condition fails, return "Spell fizzled"
    - Both condition and spell receive the same arguments
    '''
    return lambda target, power: spell(target, power) \
        if condition(target, power) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    '''
    Create spell sequence:
    - Return a function that casts all spells in order
    - Each spell receives the same arguments
    - Returns a list of all spell results
    '''
    return lambda target, power: [spell(target, power) for spell in spells]


# Grimoire
def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} fire damage"


def frostbolt(target: str, power: int) -> str:
    return f"Frostbolt freezes {target} for {power} cold damage"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with a {power} HP barrier"


if __name__ == "__main__":
    def condition(target: str, power: int) -> bool:
        return power > 10
    target = "Casie"
    power = 15

    print("Testing spell combiner...")
    combined = spell_combiner(heal, fireball)
    print(combined(target, power))

    print("\nTesting power amplifier...")
    print(f"Original: {heal(target, power)}")
    amplified = power_amplifier(heal, 3)
    print(f"Amplified: {amplified(target, power)}")

    print("\nTesting conditional caster...")
    conditional = conditional_caster(condition, frostbolt)
    print(f"Valid condition: {conditional(target, power)}")
    print(f"Invalid condition: {conditional(target, 7)}")

    print("\nTesting spell sequence...")
    spell_list = [heal, fireball, frostbolt, shield]
    sequence = spell_sequence(spell_list)
    print(sequence(target, power))
