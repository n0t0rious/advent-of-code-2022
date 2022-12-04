from helper_funcs import find_overlaps


def main():
    overlaps, semi_overlaps = find_overlaps('assignments.txt')
    print(f'Total overlaps: {overlaps}')
    print(f'Total semi-overlaps: {semi_overlaps}')


if __name__ == "__main__":
    main()
