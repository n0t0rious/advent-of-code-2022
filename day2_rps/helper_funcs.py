def get_strategy_score_1(file):
    with open('rps_strategy.txt', 'r') as file:
        score = 0
        for line in file:
            score += (score_calc(rps(line[2], line[0])))
        return score


def get_strategy_score_2(file):
    with open('rps_strategy.txt', 'r') as file:
        score = 0
        for line in file:
            score += (score_calc(rps(find_hand(line[2], line[0]), line[0])))
        return score


def rps(you: str, elf: str):
    hand = {
        'A': 1,  # Rock
        'B': 2,  # Paper
        'C': 3,  # Scissors
        'X': 1,  # Rock
        'Y': 2,  # Paper
        'Z': 3,  # Scissors

    }
    results = [None, True, False]
    return results[hand[you] - hand[elf]], hand[you]


def find_hand(condition: str, elf: str):
    conditions = {
        'X': False,  # Lose
        'Y': None,   # Draw
        'Z': True,   # Win
    }
    hand = {
        'A': 1,  # Rock
        'B': 2,  # Paper
        'C': 3,  # Scissors
    }
    results = [None, False, True]
    hands = ['X', 'Y', 'Z']

    if conditions[condition] is None:
        return hands[hand[elf] - 1]
    elif conditions[condition]:
        return hands[hand[elf] - results.index(conditions[condition]) -1]
    else:
        return hands[hand[elf] - results.index(conditions[condition]) -1]


def score_calc(result: tuple):
    return [6 + result[1] if result[0] else 3 + result[1] if result[0] is None else 0 + result[1] for i in result][0]
