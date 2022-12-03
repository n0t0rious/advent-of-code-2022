def find_duplicate_items(file):
    with open('items.txt') as items:
        duplicates = []
        for item in items:

            # split line into 2 equal compartments and convert to sets to remove duplicates

            compartment1, compartment2 = set(item[:len(item)//2]), set(item[len(item)//2:])

            for i in compartment1:
                if i in compartment2:
                    duplicates.append(i)
    return duplicates


def assign_priority(char):
    if char.islower():

        # Subtract ASCII code by 96 to obtain 1 - 26 for a-z

        return ord(char) - 96
    else:

        # Subtract ASCII code by 38 to obtain 27 - 52 for A-Z

        return ord(char) - 38


# Lambda variation of above function.
'''duplicate = map(
    lambda char: (ord(char) - 96) if char.islower() else (ord(char) - 38), find_duplicate_items('items.txt')
)'''


def find_groups(group):
    with open('items.txt') as file:
        items = [x for x in file]

        # Split lines of items into groups of 3
        elves = zip(*(iter(items),) * 3)

        groups = []
        for i in elves:

            # convert tuples to sets to remove duplicates and strip "\n" characters
            elf1, elf2, elf3 = set(i[0].strip()), set(i[1].strip()), set(i[2].strip())

            for j in elf1:
                if j in elf2 and j in elf3:
                    groups.append(j)
    return groups
