from helper_funcs import parse_stack, parse_instructions, define_stacks, rearrange_crates, get_top_crate


def main():
    # Part 1
    instructions = parse_instructions('stacks.txt')
    stacks = define_stacks(parse_stack('stacks.txt'))
    rearranged_stacks = rearrange_crates(instructions, stacks)
    get_top_crate(rearranged_stacks)

    # Part 2
    rearranged_stacks2 = rearrange_crates(instructions, define_stacks(parse_stack('stacks.txt')), crane_model=9001)
    get_top_crate(rearranged_stacks2)


if __name__ == "__main__":
    main()
