arr = []

with open('day1-input', 'r') as file:
    for line in file:
        arr.append(int(line))


for i in arr:
    for j in arr:
        for k in arr:
            if i + j + k == 2020:
                print(i*j*k)