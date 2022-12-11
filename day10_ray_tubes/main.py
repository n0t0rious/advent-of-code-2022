from helper_funcs import get_signal_strengths, create_img


def main():
	# Part 1
	print(get_signal_strengths('cycles.txt'))

	# Part 2
	create_img('cycles.txt')


if __name__ == "__main__":
	main()
