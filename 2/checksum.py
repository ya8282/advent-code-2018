#!/usr/bin/python

with open('input.txt') as f:
    box_ids = f.read().splitlines()

def count_chars(id_sequence):

    char_occurrences = {}

    for c in id_sequence:
        if c in char_occurrences:
            char_occurrences[c] += 1
        else:
            char_occurrences[c] = 1

    return char_occurrences

def count_duplicates(occurrence_dict):
    dup_two = False
    dup_three = False
    for k, v in occurrence_dict.iteritems():
        if v == 2:
            dup_two = True
        elif v == 3:
            dup_three = True
    return dup_two, dup_three


num_twos = 0
num_threes = 0
for box_id in box_ids:
    stats = count_chars(box_id)
    twos, threes = count_duplicates(stats)

    if twos == True:
        num_twos += 1

    if threes == True:
        num_threes += 1

checksum = num_twos * num_threes
print checksum
