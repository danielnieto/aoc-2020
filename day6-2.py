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
        answered_yes = dict()
        to_add = 0
        for response in group:
            for ch in response:
                if ch in answered_yes:
                    answered_yes[ch] += 1
                else:
                    answered_yes[ch] = 1

        for key, value in answered_yes.items():
            if value == len(group):
                to_add += 1

        sum += to_add

    print(sum)
