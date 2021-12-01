from itertools import combinations

def get_rates():
    rates = []
    with open('day10-sample') as file:
        for line in file:
            rates.append(int(line))
    return rates


def main():
    rates = get_rates()
    rates = sorted([0] + rates)

    combos = list(combinations(rates, 9))

    print(len(combos))



if __name__ == "__main__":
    main()