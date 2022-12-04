import re


def find_overlaps(file):
    with open(file) as file:
        assignments = [[int(i) for i in re.split(',|-', line.strip())] for line in file.readlines()]
        fully_contains = [
            (elf1 <= elf3 and elf2 >= elf4) or (elf3 <= elf1 and elf4 >= elf2)
            for elf1, elf2, elf3, elf4 in assignments]
        semi_contains = [not ((elf2 < elf3) or (elf4 < elf1)) for elf1, elf2, elf3, elf4 in assignments]
        return sum(fully_contains), sum(semi_contains)

