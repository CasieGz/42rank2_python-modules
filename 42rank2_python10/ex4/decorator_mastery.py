#!/usr/bin/env python3

from time import perf_counter, sleep
from typing import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """a decorator that measures function execution time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start

        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """ Parameterized validation decorator;
        a decorator factory that validates power levels"""
    def decorator(func: Callable):

        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power', args[-1] if args else 0)
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def trying(func: Callable):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {n}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return trying


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def wagh(power: int) -> str:
        return "Waaaaaaagh spelled !"

    print(wagh())
    print(wagh(0))

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("les carottes sont cuites"))
    print(MageGuild.validate_mage_name("occupe-toi de tes 3 oignons"))
    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Thunder", 9))
