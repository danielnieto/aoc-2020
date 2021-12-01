import re

with open('day2-input', 'r') as file:
        arr = file.read().splitlines()


pattern = '(\w+)-(\w+) (.): (.*)'

def occurrences(char, word):
    count = 0
    for c in word:
        if c == char:
            count = count + 1
    return count

def is_valid(input):
    res = re.match(pattern, input)
    min, max, char, password = res.groups()
    count = occurrences(char, password)

    return count >= int(min) and count <= int(max)


valids = 0
for pair in arr:
    if is_valid(pair):
        valids = valids + 1

print(valids)