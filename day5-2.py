
def read_passes():
    with open('day5-input', 'r') as file:
        arr = file.read().splitlines()
    return arr

def get_row(boarding_pass):
    possible = list(range(128))

    for ch in boarding_pass[0:7]:
        pivot = int(len(possible)/2)
        lower = possible[:pivot]
        upper = possible[pivot:]
        if ch == 'F':
            possible = lower
        else:
            possible = upper

    return possible[0]

def get_column(boarding_pass):
    possible = list(range(8))

    for ch in boarding_pass[-3:]:
        pivot = int(len(possible)/2)
        lower = possible[:pivot]
        upper = possible[pivot:]
        if ch == 'L':
            possible = lower
        else:
            possible = upper

    return possible[0]

def decode(boarding_pass):
    return (get_row(boarding_pass), get_column(boarding_pass))

def get_seat_id(row_and_column):
    return row_and_column[0] * 8 + row_and_column[1]


if __name__ == "__main__":
    passes = read_passes()

    seat_ids = list(map(lambda bp: get_seat_id(decode(bp)), passes))
    seat_ids.sort()

    consec = seat_ids[0]
    for i in range(len(seat_ids)):
        if seat_ids[i] == consec:
            consec += 1
        else:
            print('mine: ', consec)
            break
