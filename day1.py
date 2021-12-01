arr = []

with open('day1-input', 'r') as file:
    for line in file:
        arr.append(int(line))

target = 2020

for i in arr:

    complement = target - i

    try:
        match = arr.index(complement)
        print(i*complement)
        break
    except ValueError:
        continue
