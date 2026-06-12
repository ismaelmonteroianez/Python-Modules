def artifact_sorter(artifacts: list[dict]) -> list[dict]:
	return sorted(artifacts, key = lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
	return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
	return list(map(lambda spell: f"*{spell}*", spells))


def mage_stats(mages: list[dict]) -> dict:
	strongest_mage = max(mages, key = lambda maxp: maxp["power"])
	max_power = strongest_mage["power"]
	weakest_mage = strongest_mage = min(mages, key = lambda maxp: maxp["power"])
	min_power = weakest_mage["power"]
	total_power = 0
	for m in mages:
		total_power += m["power"]
	avg_power = round(total_power / len(mages), 2)
	return {"max_power" : max_power, "min_power" : min_power, "avg_power" : avg_power}
 

def main() -> None:
    artifacts = [
    {"name": "Fire Staff", "power": 92, "type": "staff"},
    {"name": "Crystal Orb", "power": 85, "type": "orb"},
    {"name": "Shadow Dagger", "power": 78, "type": "dagger"},
    {"name": "Storm Hammer", "power": 95, "type": "hammer"},
    {"name": "Wind Cloak", "power": 60, "type": "cloak"}
]
    mages = [
    {"name": "Aeris", "power": 40, "element": "wind"},
    {"name": "Borin", "power": 95, "element": "fire"},
    {"name": "Ciri", "power": 70, "element": "ice"},
    {"name": "Darius", "power": 30, "element": "earth"},
    {"name": "Elara", "power": 85, "element": "light"}
]
    spells = ["fireball", "heal", "shield", "ice spike", "lightning"]
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for i in range(len(sorted_artifacts) - 1):
        current = sorted_artifacts[i]
        next_artifact = sorted_artifacts[i + 1]
        print(f"{current['name']} ({current['power']} power) comes before {next_artifact['name']} ({next_artifact['power']} power)")
    print("\nTesting power filter (>= 70)...")
    filtered_mages = power_filter(mages, 70)
    for mage in filtered_mages:
        print(f"{mage['name']} - {mage['power']} power ({mage['element']})")
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print("\nTesting mage stats...")
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")

if __name__ == "__main__":
    main()
