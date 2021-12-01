PREAMBLE_LENGTH = 25

def get_list():
    with open('day9-input', 'r') as f:
        return f.read().splitlines()

def is_valid(previous, target):

    for i in range(len(previous)):
        for j in range(i+1, len(previous)):
            a = int(previous[i])
            b = int(previous[j])

            if a + b == target and a != b:
                return True

    return False


def main():
    numbers = get_list()

    for i in range(PREAMBLE_LENGTH, len(numbers)):
        previous = numbers[i - PREAMBLE_LENGTH: i]
        target = int(numbers[i])

        if not is_valid(previous, target):
            print('invalid', target)

if __name__ == "__main__":
    main()