from helper_funcs import partition_elves, find_most_calories, sort_elves, find_top_x_elves


def main():
    # Part 1
    elves_calories = partition_elves('calories.txt')
    most_calories_carried = find_most_calories(elves_calories)
    print(f'Total calories elf with most calories is carrying: {most_calories_carried}')

    # Part 2
    sorted_elves = sort_elves(elves_calories)
    top_3_elves = find_top_x_elves(sorted_elves, 3)
    print(f'Top 3 elves by calorie count: {top_3_elves}. Total calories elves are carrying = {sum(top_3_elves)}')


if __name__ == "__main__":
    main()
