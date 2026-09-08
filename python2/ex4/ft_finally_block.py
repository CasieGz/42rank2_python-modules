#!/usr/bin/env python3

class GardenError(Exception):
    """A basic error for garden problems"""

    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """For problems with plants"""

    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != (plant_name.capitalize()):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")

        water_plant("Lettuce")

        water_plant("Carrots")

    except PlantError as e:
        print(f"Caught PlantError: {e}")

    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")

        water_plant("lettuce")

        water_plant("Carrots")

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")

    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
