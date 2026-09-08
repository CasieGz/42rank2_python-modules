#!/usr/bin/env python3

class GardenError(Exception):
    """A basic error for garden problems"""

    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """For problems with plants"""

    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """For problems with watering"""

    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_water(water_level: int) -> None:
    if water_level < 2:
        raise WaterError("Not enough water in the tank!")  # instatiate with ()
    #  because without its just the class and with its creating an exept. obj.
    else:
        print("Water level is fine!")


def test_plant_healt(plant_healthy: bool, plant_name: str) -> None:
    if not plant_healthy:
        raise PlantError(f"The {plant_name} plant is wilting!")
    else:
        print("Plant is fine!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        test_plant_healt(False, "tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        test_water(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        test_plant_healt(False, "tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        test_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")
