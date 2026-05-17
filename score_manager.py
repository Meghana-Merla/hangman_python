import json


def load_scores():

    try:

        with open("scores.json", "r") as file:
            scores = json.load(file)

    except:

        scores = {}

    return scores


def save_score(player_name, score):

    scores = load_scores()

    # Update only if score is higher
    if player_name in scores:

        if score > scores[player_name]:
            scores[player_name] = score

    else:
        scores[player_name] = score

    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)


def display_high_scores():

    scores = load_scores()

    print("\n=== HIGH SCORES ===\n")

    if not scores:
        print("No scores available.")
        return

    sorted_scores = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for player, score in sorted_scores:
        print(f"{player}: {score}")