#!/usr/bin/python

# Determine the first instance of a duplicate frequency value

frequency = 0
seen_set = set()

# store file contents as parsed integer List
with open('input.txt') as f:
    seq = [ int(line.replace('\+','')) for line in f ]

found = False
while not found:
    for i in seq:
        frequency += i
        if frequency in seen_set:
            print "First duplicate: ", frequency
            found = True
            break
        else:
            seen_set.add(frequency)

