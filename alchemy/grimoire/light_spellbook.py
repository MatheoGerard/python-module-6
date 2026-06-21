from .light_validator import validate_ingredients as validate


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate_return: str = validate(ingredients)
    if "INVALID" in validate_return:
        return f"Spell rejected: {spell_name} ({validate_return})"
    return f"Spell recorded: {spell_name} ({validate_return})"
