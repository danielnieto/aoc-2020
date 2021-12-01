from os import pardir
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
    pos1, pos2, char, password = res.groups()

    pos1char = password[int(pos1)-1]
    pos2char = password[int(pos2)-1]

    return occurrences(char, f'{pos1char}{pos2char}') == 1

valids = 0
for pair in arr:
    if is_valid(pair):
        valids = valids + 1

print(valids)