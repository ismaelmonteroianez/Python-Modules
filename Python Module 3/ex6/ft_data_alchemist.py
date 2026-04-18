import random


def main() -> None:
	print("=== Game Data Alchemist ===")
	player_list = ["Alice", "bob", "Charlie", "dylan", 
				"Emma", "Gregory", "john", "kevin", "Liam"]
	print(f"Initial list of players: {player_list}")
	all_capitalized = [player.capitalize() for player in player_list]
	print(f"New list with all names capitalized: {all_capitalized}")
	only_capitalized = [player for player in player_list if player == player.capitalize()]
	print(f"New list of capitalized names only: {only_capitalized}")
	score_dict = {player:random.randint(0, 1000) for player in all_capitalized}
	print(f"Score dict: {score_dict}")
	scores = list(score_dict.values())
	average_score = sum(scores) / len(scores)
	print(f"Average score is {round(average_score, 2)}")
	only_high_scores = {key:value for key, value in score_dict.items() if value > average_score}
	print(f"High scores: {only_high_scores}")


if __name__ == "__main__":
	main()

# diccionario = {"espada": 3, "escudo": 5, "pocion": 2, "hola": 15}
# new_list = [{item: value} for item, value in diccionario.items() if value >= 3 and value < 10]
# for elemento in lista:
# 	if elemento > 5:
# 		new_list += [elemento]
#for item, value in diccionario.items():
#	print(item, value)
#print(new_list)