from copy import deepcopy

def get_code():
    with open('day8-input', 'r') as f:
        return f.read().splitlines()

def parse_code(raw_loc):
    parsed = []
    for statement in raw_loc:
        instruction, value = statement.split()
        parsed.append([instruction, int(value)])

    return parsed

def execute(loc):
    acc = 0
    pointer = 0
    executions = 0

    while(True):
        instruction = loc[pointer][0]
        value = loc[pointer][1]

        if instruction == 'nop':
            pointer += 1
        elif instruction == 'jmp':
            pointer += value
        else:
            acc += value
            pointer += 1

        executions += 1

        if executions > 9999:
            return None

        if pointer == len(loc):
            return acc


def main():
    raw_loc = get_code()
    loc = parse_code(raw_loc)

    res = None

    for i in range(len(loc)):
        msloc = deepcopy(loc)
        if msloc[i][0] == 'nop':
            msloc[i][0] = 'jmp'
        elif msloc[i][0] == 'jmp':
            msloc[i][0] = 'nop'
        else:
            continue
        res = execute(msloc)

        if res:
            print(res)
            break



if __name__ == "__main__":
    main()