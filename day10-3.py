from collections import Counter

def get_rates():
    rates = []
    with open('day10-sample') as file:
        for line in file:
            rates.append(int(line))
    return rates


def main():
    rates = get_rates()
    rates = sorted([0] + rates)

    counts = Counter({0:1})

    for rate in rates:
        for i in range(1, 4):
            counts[rate + i] += counts[rate]

    print(counts[max(rates) + 3])



if __name__ == "__main__":
    main()