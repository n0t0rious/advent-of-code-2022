with open("ropes.txt") as data:
    lines = data.read().strip().split("\n")

    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0


def is_touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(x, y):
    global head_x, head_y, tail_x, tail_y
    head_x += y
    head_y += x

    if not is_touching(head_x, head_y, tail_x, tail_y):
        sign_x = 0 if head_x == tail_x else (head_x - tail_x) / abs(head_x - tail_x)
        sign_y = 0 if head_y == tail_y else (head_y - tail_y) / abs(head_y - tail_y)

        tail_x += sign_x
        tail_y += sign_y


dd = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}

tail_visited = set()
tail_visited.add((tail_x, tail_y))

for line in lines:
    op, amount = line.split(" ")
    amount = int(amount)
    dx, dy = dd[op]

    for _ in range(amount):
        move(dx, dy)
        tail_visited.add((tail_x, tail_y))

part1 = (len(tail_visited))

