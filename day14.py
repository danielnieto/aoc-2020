from functools import reduce

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

def apply_mask(mask, decimal):
    binary = list(get_binary(decimal))
    for i, bit in enumerate(mask):
        if bit == 'X':
            continue
        binary[i] = bit

    return get_decimal(''.join(binary))

def execute(lines):
    mem = dict()
    mask = 'X'*36

    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
            continue
        mem[line[0]] = apply_mask(mask, line[1])

    return mem

def main():
    lines = get_lines()
    parsed_lines = parse_lines(lines)

    total = reduce(lambda a, b: a + b, execute(parsed_lines).values())
    print(total)


if __name__ == "__main__":
    main()