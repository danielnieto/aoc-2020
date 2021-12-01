def get_rates():
    rates = []
    with open('day10-input') as file:
        for line in file:
            rates.append(int(line))
    return rates


def main():
    rates = get_rates()
    rates.sort()
    deltas = dict()
    rates_len = len(rates)

    for i in range(rates_len):
        if i == 0:
            delta = rates[0]
        else:
            delta = rates[i] - rates[i-1]

        if delta in deltas:
            deltas[delta] += 1
        else:
            deltas[delta] = 1

    if 3 in deltas:
        deltas[3] += 1
    else:
        deltas[3] = 1

    print(deltas)
    print(deltas[1]*deltas[3])

if __name__ == "__main__":
    main()