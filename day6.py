def get_group_responses():
    groups = []
    group = []
    with open('day6-input', 'r') as f:
        for line in f:
            if line == '\n':
                groups.append(group)
                group = []
            else:
                group.append(line.replace('\n', ''))

    if len(group):
        groups.append(group)

    return groups

if __name__ == "__main__":
    groups = get_group_responses()

    sum = 0
    for group in groups:
        answered_yes = set()
        for response in group:
            for ch in response:
                answered_yes.add(ch)

        sum += len(answered_yes)

    print(sum)
