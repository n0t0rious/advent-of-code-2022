from helper_funcs import find_duplicate_items, assign_priority, find_groups


def main():
    # Part 1
    duplicates = find_duplicate_items('items.txt')

    # Map helper function to convert a-z & A-Z to numbers between 1-52
    priorities = map(assign_priority, duplicates)

    sum_priorities = sum(priorities)
    print(f'Sum of priorities: {sum_priorities}')

    # Part 2
    groups = find_groups('items.txt')
    sorted_groups = map(assign_priority, groups)
    sum_group_priorities = sum(sorted_groups)
    print(f'Sum of group priorities: {sum_group_priorities}')


if __name__ == "__main__":
    main()
