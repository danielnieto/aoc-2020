def get_code():
    with open('day8-input', 'r') as f:
        return f.read().splitlines()

def parse_code(raw_loc):
    parsed = []
    for statement in raw_loc:
        instruction, value = statement.split()
        parsed.append((instruction, int(value)))

    return parsed

def execute(loc):
    history = []
    acc = 0
    pointer = 0

    while(True):
        instruction = loc[pointer][0]
        value = loc[pointer][1]

        if pointer in history:
            break

        history.append(pointer)

        if instruction == 'nop':
            pointer += 1
        elif instruction == 'jmp':
            pointer += value
        else:
            acc += value
            pointer += 1

    print(acc)


if __name__ == "__main__":
    raw_loc = get_code()
    loc = parse_code(raw_loc)
    execute(loc)
