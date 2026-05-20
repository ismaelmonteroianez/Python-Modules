def main() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(f"Testing record dark spell"
          f": {dark_spell_record('Infernal', 'bats frogs')}")


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    main()
