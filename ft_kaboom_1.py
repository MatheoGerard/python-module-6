if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grimoire.dark_spellbook as spell

    print(
        "Testing record light spell: "
        f"{spell.dark_spell_record('Fantasy', 'Earth, wind, fire')}"
    )
