from helper import Folder, traverse_files


def main():
	# Part 1
	print(traverse_files('directories.txt'))

	# Part 2
	print(traverse_files('directories.txt', part1=False))


if __name__ == "__main__":
	main()
