from stack_class import Stack
import re


def parse_stack(file):
    # loops through each column in stack matrix and parses values based on distance between letter elements
    stacks = []
    for i in range(1, 37, 4):
        with open('stacks.txt') as file:
            data = [file.readline()[i].strip() for _ in range(number_of_stacks())]
        stacks.append(list(filter(bool, data)))
    return stacks


def parse_instructions(file):
    # parses number values in instructions into tuple e.g. move 3 from 9 to 6 -> (3,9,6)
    with open(file) as instructions:
        box_instructions = [re.findall(r'\d+', line) for line in instructions.readlines()[10:]]
        box_instructions = [tuple([int(i) for i in j]) for j in box_instructions]
    return box_instructions


def define_stacks(stack_list: list):
    # converts each stack in the list of stacks into a Stack class
    stacks = []
    for s in stack_list:
        stack = Stack(s[::-1])
        stacks.append(stack)
    return stacks


def get_stacks(stacks: tuple, stack_list):
    # retrieves stacks to work with based on values in tuple from parse_instructions e.g. (3,9,6)
    # first element: specifies move, second: stack to move from, third, stack to move to
    return stack_list[stacks[0]-1], stack_list[stacks[1]-1]


def rearrange_crates(instructions: list, stacks_list: list, crane_model: int = 9000):
    # 9000 crane model for part 1, 9001 crane model for part 2
    if crane_model == 9000:
        stack = stacks_list
        for instruction in instructions:
            current_stack, new_stack = get_stacks((instruction[1], instruction[2]), stack)
            for _ in range(instruction[0]):
                popped = current_stack.pop()
                new_stack.push(popped)
        return stacks_list

    elif crane_model == 9001:
        stack = stacks_list
        for instruction in instructions:
            to_be_moved = []
            current_stack, new_stack = get_stacks((instruction[1], instruction[2]), stack)
            for _ in range(instruction[0]):
                to_be_moved.append(current_stack.pop())
            for i in range(1, len(to_be_moved)+1):
                new_stack.push(to_be_moved[-i])
        return stacks_list

    else:
        raise TypeError


def get_top_crate(stacks_list: list):
    for stack in stacks_list:
        print(stack.peek())


def number_of_stacks():
    # returns number of stacks based on positioning of last stack number in txt file
    with open('stacks.txt') as file:
        return int((file.readlines()[8][len(file.readline())-2]))-1
