with open("ropes.txt") as fin:
    lines = fin.read().strip().split("\n")


knots = [[0, 0] for _ in range(10)]


def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(x, y):
    global knots
    knots[0][0] += x
    knots[0][1] += y

    for i in range(1, 10):
        head_x, head_y = knots[i - 1]
        tail_x, tail_y = knots[i]

        if not touching(head_x, head_y, tail_x, tail_y):
            sign_x = 0 if head_x == tail_x else (head_x - tail_x) / abs(head_x - tail_x)
            sign_y = 0 if head_y == tail_y else (head_y - tail_y) / abs(head_y - tail_y)

            tail_x += sign_x
            tail_y += sign_y

        knots[i] = [tail_x, tail_y]


dd = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}

tail_visited = set()
tail_visited.add(tuple(knots[-1]))

for line in lines:
    op, amount = line.split(" ")
    amount = int(amount)
    x, y = dd[op]

    for _ in range(amount):
        move(x, y)
        tail_visited.add(tuple(knots[-1]))

part2 = len(tail_visited)