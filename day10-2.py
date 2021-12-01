from functools import lru_cache

def get_rates():
    rates = []
    with open('day10-input') as file:
        for line in file:
            rates.append(int(line))
    return rates

@lru_cache
def main():
    rates = get_rates()
    rates.sort()
    combos = [[0]]

    for i in range(len(rates)):
        val = rates[i]
        for j in range(len(combos)):
            combo = combos[j]
            delta = val - combo[-1]
            if delta >= 0 and delta <= 3:
                new_combo = combo[:]
                new_combo.append(val)
                combos.append(new_combo)

    # for i in range(len(rates)):
    #     val = rates[i]
    #     j = 0
    #     print(f'{i}/{len(rates)}')
    #     while(True):
    #         combo = combos[j]
    #         delta = val - combo[-1]

    #         if delta >= 0 and delta <= 3:
    #             new_combo = combo[:]
    #             new_combo.append(val)
    #             combos.append(new_combo)
    #             j = j + 2
    #         else:
    #             combos.remove(combo)

    #         if j == len(combos):
    #             break

    print('result', len(list(filter(lambda c: c[-1] == rates[-1], combos))))

  
    



if __name__ == "__main__":
    # main()

    with open("day10-input") as f:
        l = [0] + sorted(list(map(int, f.read().splitlines())))
    @lru_cache
    def solution(n=0):
        return (n == len(l) - 1) + sum(
            solution(j) for j in range(n + 1, len(l)) if l[n] + 3 >= l[j]
        )
    print(solution())