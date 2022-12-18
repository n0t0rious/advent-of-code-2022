from helper_funcs import parse_input, find_visible_trees, find_scenic_score


def main():
	grid = parse_input('trees.txt')
	visible_trees = find_visible_trees(grid)
	print(visible_trees)


	# Part 2
	scenic_score = find_scenic_score(grid)
	print(scenic_score)


if __name__ == "__main__":
	main()
