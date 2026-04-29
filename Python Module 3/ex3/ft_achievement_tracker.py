import random


def gen_player_achievements() -> set[str]:
    achievement_list = ['Crafting Genius', 'Strategist',
                        'World Savior', 'Speed Runner', 'Survivor',
                        'Master Explorer', 'Treasure Hunter',
                        'Unstoppable', 'First Steps',
                        'Collector Supreme', 'Untouchable', 'Sharp Mind',
                        'Boss Slayer', 'Hidden Path Finder']
    random_number = random.randint(5, 10)
    player_achievements = set(random.sample(achievement_list, k=random_number))
    return (player_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice_achievements = gen_player_achievements()
    print(f"Player Alice: {alice_achievements}")
    bob_achievements = gen_player_achievements()
    print(f"Player Bob: {bob_achievements}")
    charlie_achievements = gen_player_achievements()
    print(f"Player Charlie: {charlie_achievements}")
    dylan_achievements = gen_player_achievements()
    print(f"Player Dylan: {dylan_achievements}\n")
    common_achievements = alice_achievements.intersection(
        bob_achievements,
        charlie_achievements, dylan_achievements
        )
    all_achievements = alice_achievements.union(
        bob_achievements,
        charlie_achievements, dylan_achievements
        )
    print(f"All distinct achievements: {all_achievements}\n")
    print(f"Common achievements: {common_achievements}\n")
    only_alice = alice_achievements.difference(
        bob_achievements, charlie_achievements, dylan_achievements)
    print(f"Only Alice has: {only_alice}")
    only_bob = bob_achievements.difference(
        alice_achievements, charlie_achievements, dylan_achievements)
    print(f"Only Bob has: {only_bob}")
    only_charlie = charlie_achievements.difference(
        alice_achievements, bob_achievements, dylan_achievements)
    print(f"Only Charlie has: {only_charlie}")
    only_dylan = dylan_achievements.difference(
        alice_achievements, bob_achievements, charlie_achievements)
    print(f"Only Dylan has: {only_dylan}\n")
    achievement_list = {'Crafting Genius', 'Strategist',
                        'World Savior', 'Speed Runner', 'Survivor',
                        'Master Explorer', 'Treasure Hunter',
                        'Unstoppable', 'First Steps',
                        'Collector Supreme', 'Untouchable', 'Sharp Mind',
                        'Boss Slayer', 'Hidden Path Finder'}
    print("Alice is missing: "
          f"{achievement_list.difference(alice_achievements)}")
    print(f"Bob is missing: {achievement_list.difference(bob_achievements)}")
    print("Charlie is missing: "
          f"{achievement_list.difference(charlie_achievements)}")
    print("Dylan is missing: "
          f"{achievement_list.difference(dylan_achievements)}")


if __name__ == "__main__":
    main()
