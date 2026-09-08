#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        extract_key_value = arg.split(":")  # split input at colon
        if len(extract_key_value) != 2:   # is less or more than two arguments?
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name: str = extract_key_value[0]  # first word is the key
        try:
            quantity = int(extract_key_value[1])  # second one the value
        except ValueError as e:  # is it an int?
            print(f"Quantity error for '{extract_key_value[0]}': {e}")
            continue
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
        else:
            inventory[item_name] = quantity

    if inventory:
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        total_quantity: int = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} "
              f"items: {total_quantity}")
        for item in inventory:
            percentage = (inventory[item] / total_quantity) * 100
            print(f"Item {item} represents: {round(percentage, 1)}%")

    # Getting most abundant item
        first_key = list(inventory.keys())[0]  # start comparing with that

        most_abundant_item = first_key
        highest_quantity = inventory[first_key]
        for item in inventory.keys():  # go through all keys
            if inventory[item] > highest_quantity:
                highest_quantity = inventory[item]  # store value
                most_abundant_item = item  # store key
        print(f"Item most abundant: {most_abundant_item} with quantity "
              f"{inventory[most_abundant_item]}")

    # Getting least abundant item
        least_abundant_item = first_key
        lowest_quantity = inventory[first_key]
        for item in inventory.keys():  # go through all keys
            if inventory[item] < lowest_quantity:
                lowest_quantity = inventory[item]  # store value
                least_abundant_item = item  # store key
        print(f"Item least abundant: {least_abundant_item} with quantity "
              f"{inventory[least_abundant_item]}")

        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
    else:
        print("Inventory is empty.")
