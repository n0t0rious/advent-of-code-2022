def get_signal_strengths(file, cycle=1, cycle_num=0):
    signals = []
    with open(file) as data:
        cycles = data.read().split("\n")
        for i, cmd in enumerate(cycles):
            if cmd == 'noop':
                cycle_num += 1
                if (cycle_num - 20) % 40 == 0:
                    signals.append(cycle_num * cycle)
            else:
                for _ in range(0, 2):
                    cycle_num += 1
                    if (cycle_num - 20) % 40 == 0:
                        signals.append(cycle_num * cycle)
                cycle += int(cycles[i][4:])
    return sum(signals)


def create_img(file, cycle=1, cycle_num=0):
    pixels = list("." * 40 * 6)

    def update_pixels(cycle, cycles, pixels):
        pos = (cycles - 1) % 40
        if pos in {cycle - 1, cycle, cycle + 1}:
            pixels[cycles - 1] = "#"

    with open(file) as file:
        data = file.read().split("\n")
        for i, cmd in enumerate(data):
            if cmd == 'noop':
                cycle_num += 1
                update_pixels(cycle, cycle_num, pixels)
            else:
                cycle_num += 1
                update_pixels(cycle, cycle_num, pixels)
                cycle_num += 1
                update_pixels(cycle, cycle_num, pixels)
                cycle += int(data[i][4:])
    for i in range(0, 201, 40):
        print("".join(pixels[i: i + 40]))
    return 0
