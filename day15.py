from collections import Counter

def get_input():
    return [7,14,0,17,11,1,2]

def main():
    spoken = get_input()[:]

    for i in range(len(spoken), 2020):
        lns = spoken[-1]
        c = Counter(spoken)
        if c[lns] == 1:
            spoken.append(0)
        elif c[lns] > 1:
            turns = [i for i, num in enumerate(spoken) if num == lns]
            delta = turns[-1] - turns[-2]
            spoken.append(delta)

    print(spoken[-1])

 

if __name__ == "__main__":
    main()