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
    """Simulates rock paper scissors with input from strategy file and returns True for win,
    False for loss, None for draw"""

    # Determine winner of rps using negative indexing of lists
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
    """Returns hand needed to obtain given game condition ( Win, Draw, Lose)"""

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

    '''Validates bool values and uses elf's hand and desired outcome to index hand to pass into rps function to obtain
    desired game outcome'''
    if conditions[condition] is None:
        return hands[hand[elf] - 1]
    elif conditions[condition]:
        return hands[hand[elf] - results.index(conditions[condition]) - 1]
    else:
        return hands[hand[elf] - results.index(conditions[condition]) - 1]


def score_calc(result: tuple):
    """Returns score taking into account Win, Loss, Draw and extra point awarded for hand played"""

    # Calculate score using bool values to validate
    return [6 + result[1] if result[0] else 3 + result[1] if result[0] is None else 0 + result[1] for i in result][0]
