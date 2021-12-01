def get_array_from_rule(rule):
    expanded = []

    lhs, rhs = rule.split(' or ')

    lhs_min, lhs_max = lhs.split('-')
    rhs_min, rhs_max = rhs.split('-')

    for i in range(int(lhs_min), int(lhs_max) + 1):
        if not i in expanded:
            expanded.append(i)

    for i in range(int(rhs_min), int(rhs_max) + 1):
        if not i in expanded:
            expanded.append(i)

    return expanded


def get_input():

    section = 0
    rules = []
    my_ticket = None
    nearby = []
    for line in open('day16.txt'):

        if line == '\n':
            section += 1
            continue

        line = line.strip()

        if section == 0:
            rules.append(get_array_from_rule(line.split(': ')[1]))
        elif section == 1:
            if line == 'your ticket:':
                continue
            my_ticket = [int(val) for val in line.split(',')]
        else:
            if line == 'nearby tickets:':
                continue
            nearby.append([int(val) for val in line.split(',')])

    return (rules, my_ticket, nearby)

def check_invalid_ticket(rules, ticket):

    invalid_values = []

    for v in ticket:
        fails = 0
        for rule in rules:
            if v not in rule:
                fails += 1

        if fails == len(rules):
            invalid_values.append(v)
    return invalid_values


def main():

    rules, my_ticket, nearby = get_input()

    sum = 0

    for i, ticket in enumerate(nearby):
        for invalid in check_invalid_ticket(rules, ticket):
            sum += invalid

    for invalid in check_invalid_ticket(rules, my_ticket):
            sum += invalid

    print('result', sum)

if __name__ == "__main__":
    main()