from copy import deepcopy

def get_layout():
    return [list(line.strip()) for line in open('day11-input.txt')]

def get_first_seat(dh, dv, row, col, layout):
    pos_row = row
    pos_col = col
    while(True):
        pos_row += dv
        pos_col += dh

        if pos_row < 0 or pos_row > len(layout) - 1:
            break

        if pos_col < 0 or pos_col > len(layout[0]) - 1:
            break

        if layout[pos_row][pos_col] != '.':
            return layout[pos_row][pos_col]

    return None

def get_first_seats(row,col,layout):
    seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            seats.append(get_first_seat(i,j,row, col, layout))
    return seats

def get_occupied_count(seats):
    count = 0
    if not seats:
        return 0
    for seat in seats:
        if seat == '#':
            count += 1
    return count


def main():
    layout = get_layout()

    previous_layout = deepcopy(layout)
    total_occupied_count = 0

    while(True):
        new_layout = deepcopy(previous_layout)
        total_occupied_count = 0
        for x, row in enumerate(previous_layout):
            for y, column in enumerate(row):
                occupied = get_occupied_count(get_first_seats(x,y, previous_layout))
                if column == 'L' and occupied == 0:
                    new_layout[x][y] = '#'
                elif column == '#' and occupied >= 5:
                    new_layout[x][y] = 'L'

                if new_layout[x][y] == '#':
                    total_occupied_count += 1

        if new_layout == previous_layout:
            break
        else:
            previous_layout = deepcopy(new_layout)

    print('done', total_occupied_count)


if __name__ == "__main__":
    main()