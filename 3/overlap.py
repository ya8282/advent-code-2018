#!/usr/bin/python

def data_from_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append([int(x) for x in line.split(',')])
    return data

def plan_grid(patches):
    grid = []
    for i in range(2000): #TODO: calculate on the fly
        grid.append([])
        for j in range(2000):
            grid[i].append(0)

    for i in patches:
        x = int(i[0])
        y = int(i[1])
        width = int(i[2])
        height = int(i[3])

        for n in range(x, x+width):
            for m in range(y, y+height):
                grid[n][m] += 1

    return grid

def count_overlaps(grid):
    total = 0
    for row in grid:
        total += sum(1 for i in row if i > 1)
    return total


grid = plan_grid(data_from_file('input2.txt'))
print count_overlaps(grid)
