def get_input():
    with open('day13-input.txt') as f:
        lines = f.read().splitlines()
        buses = []
        for bus in lines[1].split(','):
            if bus == 'x':
                buses.append(-1)
                continue
            buses.append(int(bus))
    return (int(lines[0]), buses)

def main():
    _, buses = get_input()

    current = 100000000000000
    result = None
    while(result == None):
        for i, bus in enumerate(buses):

            if bus == -1:
                continue

            if (current + i) % bus != 0:
                break

            if bus == buses[-1]:
                result = current

        current += buses[0]
        print(current)

    print(result)

if __name__ == "__main__":
    main()