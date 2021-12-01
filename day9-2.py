PREAMBLE_LENGTH = 25

def get_list():
    with open('day9-input', 'r') as f:
        return f.read().splitlines()

def parse_numbers(list):
    numbers = []

    for i in list:
        numbers.append(int(i))
    return numbers

def is_valid(previous, target):

    for i in range(len(previous)):
        for j in range(i+1, len(previous)):
            a = previous[i]
            b = previous[j]

            if a + b == target and a != b:
                return True

    return False

def main():
    numbers = parse_numbers(get_list())
    invalid = None
    weakness = None

    for i in range(PREAMBLE_LENGTH, len(numbers)):
        previous = numbers[i - PREAMBLE_LENGTH: i]
        target = numbers[i]

        if not is_valid(previous, target):
            invalid = target
            break

    for i in range(len(numbers)):
        acc = numbers[i]
        for j in range(i + 1, len(numbers)):
            acc += numbers[j]

            if acc == invalid:
                weak_range = numbers[i:j+1]
                weak_range.sort()
                weakness = weak_range[0] + weak_range[-1]
                break;

    print(weakness)


if __name__ == "__main__":
    main()