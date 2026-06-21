import elements as par_elem
from alchemy import elements as loc_elem


def healing_potion() -> str:
    return (
        f"Healing potion brewed with ’{loc_elem.create_earth()}’"
        " and ’{loc_elem.create_air()}’"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with ’{par_elem.create_fire()}’"
        " and ’{par_elem.create_water()}’"
    )
