from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredient_list = ingredients.lower().replace(",", " ").split()
    allowed_ingredients = light_spell_allowed_ingredients()

    is_valid = any(item in ingredient_list for item in allowed_ingredients)

    status = "VALID" if is_valid else "INVALID"

    return f"{ingredients} - {status}"
