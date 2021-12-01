import functools

with open('day3-input', 'r') as file:
        arr = file.read().splitlines()


for i in range(0, len(arr)):
    arr[i] = arr[i] * 500


def how_many_trees(dx, dy):
    x = 0
    y = 0
    trees = 0

    while y < len(arr) - dy:
        x = x + dx
        y = y + dy

        if arr[y][x] == "#":
            trees += 1
    return trees

results = [
    how_many_trees(1,1),
    how_many_trees(3,1),
    how_many_trees(5,1),
    how_many_trees(7,1),
    how_many_trees(1,2),
]

print(functools.reduce(lambda a,b : a*b, results))