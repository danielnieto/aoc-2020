from itertools import combinations

arr = []

with open('day1-input', 'r') as file:
    for line in file:
        arr.append(int(line))

print(list(combinations(arr, 100)))

