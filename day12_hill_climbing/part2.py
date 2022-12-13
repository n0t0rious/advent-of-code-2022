from heapq import heappop, heappush
from string import ascii_lowercase

# def parse_input(file):
with open('hills.txt') as data:
    hill_data = data.read().strip().split()
    grid = [list(hill) for hill in hill_data]
    n = len(grid)
    m = len(grid[0])

    # find starting index by looping through grid and setting start to index of S, end ndex E
    for i in range(n):
        for j in range(m):
            char = grid[i][j]
            if char == "S":
                start = i, j
            if char == "E":
                end = i, j

    # map height to each letter, set 0 for S (Start), 25 for E (End)
    def find_height(letter):
        if letter in ascii_lowercase:
            return ascii_lowercase.index(letter)
        if letter == "S":
            return 0
        if letter == "E":
            return 25


    def valid_neighbors(i, j):
        # define down, up, right, left
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ii = i + di
            jj = j + dj
        # check location is within the map
            if not (0 <= ii < n and 0 <= jj < m):
                continue
            if find_height((grid[ii][jj])) >= find_height(grid[i][j]) - 1:
                yield ii, jj

    visited = [[False] * m for _ in range(n)]
    heap = [(0, end[0], end[1])]

    while True:
        steps, i, j = heappop(heap)

        if visited[i][j]:
            continue
        visited[i][j] = True

        if find_height(grid[i][j]) == 0:
            print(steps)
            break

        for ii, jj in valid_neighbors(i, j):
            heappush(heap, (steps + 1, ii, jj))
