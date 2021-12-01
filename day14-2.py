from functools import reduce
from copy import deepcopy

def get_lines():
    return [line.strip() for line in open('day14.txt')]

def parse_lines(lines):
    parsed = []
    for line in lines:
        lhs, rhs = line.split(' = ')

        if lhs == 'mask':
            parsed.append((
                lhs, rhs
            ))
        else:
            parsed.append((
                int(lhs[lhs.index('[')+1:-1]), int(rhs)
            ))
    return parsed

def get_binary(decimal):
    return '{0:036b}'.format(decimal)

def get_decimal(binary):
    return int(binary, 2)

def get_all_values_from_mask(mask, decimal):
    binary = list(get_binary(decimal))

    values = [[]]
    result = []

    for i, bit in enumerate(mask):
        if bit == '0':
            continue
        binary[i] = bit

    for i, bit in enumerate(binary):

        if bit == 'X':
            values1 = deepcopy(values)
            values2 = deepcopy(values)

            for i in values1:
                i.append('0')

            for i in values2:
                i.append('1')

            values = values1 + values2
        else:
            for i in values:
                i.append(bit)

    for value in values:
        result.append(get_decimal(''.join(value)))

    return result


def execute(lines):
    mem = dict()
    mask = 'X'*36

    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
            continue
        addresses = get_all_values_from_mask(mask, line[0])
        for address in addresses:
            mem[address] = line[1]

    return mem

def main():
    lines = get_lines()
    parsed_lines = parse_lines(lines)

    total = reduce(lambda a, b: a + b, execute(parsed_lines).values())
    print(total)


if __name__ == "__main__":
    # main_debug()
    main()