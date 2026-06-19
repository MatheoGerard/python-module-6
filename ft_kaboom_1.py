import alchemy.grimoire.dark_spellbook as spell

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(
        f"Testing record light spell: {spell.dark_spell_record('Fantasy', 'Earth, wind, fire')}"
    )
