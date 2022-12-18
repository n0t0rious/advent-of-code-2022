import numpy as np


def parse_input(file):
    with open(file, 'r') as data:
        trees = data.read().strip().split()
        count = 0
        trees = [[int(tree) for tree in row] for row in trees]
        return trees


def find_visible_trees(trees):
    grid = np.array(trees)
    n = len(trees)
    m = len(trees[0])
    visible = 0
    for i in range(n):
        for j in range(m):
            height = grid[i, j]
            if j == 0 or np.amax(grid[i, :j]) < height:
                visible += 1
            elif j == m - 1 or np.amax(grid[i, (j+1):]) < height:
                visible += 1
            elif i == 0 or np.amax(grid[:i, j]) < height:
                visible += 1
            elif i == n - 1 or np.amax(grid[(i+1):, j]) < height:
                visible += 1
    return visible


def find_scenic_score(trees):
    grid = np.array(trees)
    n = len(trees)
    m = len(trees[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    scenic_score = 0

    for i in range(n):
        for j in range(m):
            h = grid[i, j]
            score = 1
            for di, dj in directions:
                ii, jj = i + di, j + dj
                dist = 0
                while (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] < h:
                    dist += 1
                    ii += di
                    jj += dj
                    if (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] >= h:
                        dist += 1
                score *= dist
            scenic_score = max(scenic_score, score)
    return scenic_score
