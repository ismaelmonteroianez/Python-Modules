import sys


def main() -> None:
    scores = []
    print("=== Player Score Analytics ===")
    valid_arguments = False
    for i in range(1, len(sys.argv)):
        try:
            number = int(sys.argv[i])
            scores = scores + [number]
            valid_arguments = True
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if not valid_arguments:
        print("No scores provided."
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    total_players = len(scores)
    print(f"Total players: {total_players}")
    total_score = sum(scores)
    print(f"Total score: {total_score}")
    print(f"Average score: {sum(scores) / len(scores)}")
    max_score = max(scores)
    print(f"High score: {max_score}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
