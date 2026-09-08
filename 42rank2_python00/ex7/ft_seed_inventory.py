def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        unit_label = f"{quantity} packets available"
    elif unit == "grams":
        unit_label = f"{quantity} grams total"
    elif unit == "area":
        unit_label = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type} seeds: {unit_label}")
