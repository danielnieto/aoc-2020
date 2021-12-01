
from collections import Counter
import time

def get_input():
    return [7,14,0,17,11,1,2]

def main():
    start_time = time.time()

    spoken = get_input()[:]
    target = 30000000

    c = Counter(spoken)

    ct = {}

    for turn, initial in enumerate(spoken):
        ct[initial] = [turn]

    for i in range(len(spoken), target):
        if i%1000000 == 0:
            print(f'{(i/target)*100}%')
        lns = spoken[-1]
        if c[lns] == 1:
            c[0] += 1
            spoken.append(0)
            if 0 in ct:
                ct[0].append(i)
            else:
                ct[0] = [i]
        elif c[lns] > 1:
            turns = ct[lns]
            delta = turns[-1] - turns[-2]
            c[delta] += 1
            spoken.append(delta)
            if delta in ct:
                ct[delta].append(i)
            else:
                ct[delta] = [i]

    print(spoken[-1])
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()