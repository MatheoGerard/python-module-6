from .. import elements as al_elem
from .. import potions as pot
import elements


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew ’{al_elem.create_air()}’ and ’{pot.strength_potion()}’ mixed with ’{elements.create_fire()}’"
