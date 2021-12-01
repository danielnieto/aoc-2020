from copy import deepcopy

def get_input():
    with open('day13.txt') as f:
        lines = f.read().splitlines()
        buses = []
        for bus in lines[1].split(','):
            if bus == 'x':
                continue
            buses.append(int(bus))
    return (int(lines[0]), buses)

def main():
    inp = get_input()

    target = inp[0]
    current = deepcopy(target)
    result = None
    while(result == None):
        for bus in inp[1]:
            if current % bus == 0:
                result = (current - target) * bus
                break
        current += 1
    print(result)

if __name__ == "__main__":
    main()