from .dark_validator import dark_validate_ingredients as validate


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str):
    validate_return: str = validate(ingredients)
    if "INVALID" in validate_return:
        return f"Spell rejected: {spell_name} ({validate_return})"
    elif "VALID" in validate_return:
        return f"Spell recorded: {spell_name} ({validate_return})"
