#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    for temp_str in ("25", "abc"):
        try:
            print(f"Input data is '{temp_str}'")
            temp_int: int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C\n")
        except ValueError as e:  # e is just a random
            # name where the ValueError then is stored
            print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
