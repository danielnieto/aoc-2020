def get_input():
    with open('day13.txt') as f:
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

    current = buses[0]
    result = None
    increment = buses[0]
    pos = 1
    lcm = buses[0]
    while(result == None):
        while(buses[pos] == -1 ):
            pos += 1
        if (current + pos) % buses[pos] == 0:
            lcm *= buses[pos]
            increment = lcm

            pos += 1

            if pos == len(buses):
                print('final', current)
                break

        current += increment

    print(result)

if __name__ == "__main__":
    main()