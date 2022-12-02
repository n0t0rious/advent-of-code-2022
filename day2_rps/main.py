from helper_funcs import get_strategy_score_1, get_strategy_score_2


def main():
    # Part 1
    strategy1_score = get_strategy_score_1('rps_strategy.txt')
    print(f'Total score: {strategy1_score}')

    # Part 2
    strategy2_score = get_strategy_score_2('rps_strategy.txt')
    print(f'Total score: {strategy2_score}')


if __name__ == "__main__":
    main()
