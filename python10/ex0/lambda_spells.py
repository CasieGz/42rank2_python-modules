#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    '''
    Sort magical artifacts:
    - Use sorted() with a lambda to sort by ’power’ level (descending)
    - Each artifact is a dict: {’name’: str, ’power’: int, ’type’: str}
    - Return the sorted list
    '''

    return sorted(
        artifacts,
        key=lambda a: a["power"],
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    '''
    Filter mages by power:
    - Use filter() with a lambda to find mages with power >= min_power
    - Each mage is a dict: {’name’: str, ’power’: int, ’element’: str}
    - Return a list of filtered mages
    '''
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    '''
    Transform spell names:
    - Use map() with a lambda to add "* " prefix and " *" suffix
    - Input: list of spell names (strings)
    - Return a list of transformed spell names
    '''
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    '''
    Calculate statistics:
    - Use lambdas with max(), min() to find:
    - Most powerful mage’s power level
    - Least powerful mage’s power level
    - Average power level (rounded to 2 decimals)
    - Returndict: {’max_power’: int, ’min_power’: int, ’avg_power’: float}
    '''
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    total = sum(map(lambda m: m["power"], mages))
    avg_power = round(total / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts: list[dict[str, str | int]] = [
        {"name": "Crystal Orb", "power": 85, "type": "Arcane"},
        {"name": "Fire Staff", "power": 92, "type": "Fire"},
        {"name": "Shadow Dagger", "power": 78, "type": "Shadow"},
    ]
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    if len(sorted_artifacts) >= 2:
        first = sorted_artifacts[0]
        second = sorted_artifacts[1]
        print(f"{first['name']} ({first['power']} power) comes before "
              f"{second['name']} ({second['power']} power)")

    mages: list[dict[str, str | int]] = [
        {"name": "Ice Wand", "power": 64, "element": "Frost"},
        {"name": "Fire Staff", "power": 92, "element": "Fire"},
        {"name": "Thunder Bow", "power": 88, "element": "Lightning"}
    ]
    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 70)
    for mage in filtered_mages:
        print(f"- {mage['name']} (Power: {mage['power']})")

    spells = ["fireball", "heal", "shield"]
    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(spell for spell in transformed_spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Average Power: {stats['avg_power']}")
