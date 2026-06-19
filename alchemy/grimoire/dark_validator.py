from .dark_spellbook import dark_spell_allowed_ingredients as spell_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = spell_ingredients()
    ingredients_list: list[str] = ingredients.split(" ")
    for x in ingredients_list:
        for y in allowed_ingredients:
            if x.lower() == y.lower():
                return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
