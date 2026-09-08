#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        if raw_input.count(",") != 2:
            print("Invalid syntax")
            continue
        coordinates = raw_input.split(",")  # splits string at each comma
        i: int = 0  # need index to show specific error
        try:
            x = float(coordinates[i].strip())  # strips all whitespace
            i += 1
            y = float(coordinates[i].strip())
            i += 1
            z = float(coordinates[i].strip())

            return (x, y, z)

        except ValueError as e:
            print(f"Error on parameter '{coordinates[i].strip()}': {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    first_coordinates = get_player_pos()
    print(f"Got a first tuple: {first_coordinates}")

    x1, y1, z1 = first_coordinates  # unpacking tuples
    # meaning storing the seperate tuple values in new variables for us to use
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance_to_center = round(
        math.sqrt((0 - x1)**2 + (0 - y1)**2 + (0 - z1)**2), 4)
    # ** means to the power of (what comes after the asterisks)
    # for the distance to center my second coordinates are (0,0,0)
    print(f"Distance to center: {distance_to_center}")

    print("\nGet a second set of coordinates")
    second_coordinates = get_player_pos()

    x2, y2, z2 = second_coordinates
    distance_between_coordinates = round(
        math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4)
    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_between_coordinates}")
