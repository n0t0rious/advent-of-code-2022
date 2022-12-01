import re
from itertools import groupby


def partition_elves(file):
    """Takes day 1 input as a txt file and returns list of lists containing each elf's calorie data"""
    # open txt file and initialize calories list
    with open(file, "r") as file:
        calories = []

        # replace new line characters with ''
        for x in file:
            calories.append(re.sub('\n', '', x))

        # split by '' to get list of lists, each list represents 1 elf and respective calorie count for their food items
        elves = [list(g) for k, g in groupby([int(calorie) if calorie.isdigit() else '' for calorie in calories],
                                             key=bool) if k]
    return elves


def find_most_calories(elves: list[[]]):
    """Takes list of lists, each list representing an elf, each value representing a food item and returns the elf
    carrying the most calories"""
    max_calories = 0
    for elf in elves:
        if sum(elf) > max_calories:
            max_calories = sum(elf)
    return max_calories


def sort_elves(elves: list):
    """Sorts elves by total calorie count in descending order"""
    total_calories = [sum(calories) for calories in elves]
    return sorted(total_calories, reverse=True)


def find_top_x_elves(elves: list, x: int):
    """Returns list of top 'x' elves by largest calorie count"""
    try:
        return elves[0:x]
    except IndexError as e:
        print(e)
