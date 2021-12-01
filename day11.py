from copy import deepcopy

def get_layout():
    return [list(line.strip()) for line in open('day11-input.txt')]

def get_adjacent(x,y, layout):
    adjacent = []

    for ix in range(x - 1, x + 2):
        if ix < 0 or ix > len(layout) - 1:
            continue
        for iy in range(y - 1, y + 2):
            if iy < 0 or iy > len(layout[0]) - 1:
                continue
            if ix == x and iy == y:
                continue
            adjacent.append(layout[ix][iy])

    return adjacent

def get_occupied_count(seats):
    count = 0
    for seat in seats:
        if seat == '#':
            count += 1
    return count


def main():
    layout = get_layout()
    previous_layout = deepcopy(layout)
    final_layout = None
    total_occupied_count = 0

    while(True):
        new_layout = deepcopy(previous_layout)
        total_occupied_count = 0
        for x, row in enumerate(previous_layout):
            for y, column in enumerate(row):
                occupied = get_occupied_count(get_adjacent(x,y, previous_layout))
                if column == 'L' and occupied == 0:
                    new_layout[x][y] = '#'
                elif column == '#' and occupied >= 4:
                    new_layout[x][y] = 'L'

                if new_layout[x][y] == '#':
                    total_occupied_count += 1

        if new_layout == previous_layout:
            final_layout = new_layout
            break
        else:
            previous_layout = deepcopy(new_layout)

    print('done', total_occupied_count)


if __name__ == "__main__":
    main()