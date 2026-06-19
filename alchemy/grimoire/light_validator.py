def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients as spell_ingredients

    allowed_ingredients: list[str] = spell_ingredients()
    ingredients_list: list[str] = ingredients.split(" ")
    for x in ingredients_list:
        for y in allowed_ingredients:
            if x.lower() == y.lower():
                return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
