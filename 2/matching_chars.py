#!/usr/bin/python

with open('input.txt') as f:
    box_ids = f.read().splitlines()


def matches(w1, w2):
    min_len = min(len(w1),len(w2))
    common_chars = 0
    common_word = ""
    for i in xrange(min_len):
        if w1[i] == w2[i]:
            common_chars += 1
            common_word += w1[i]
    return common_word, common_chars


def match_list(ids):
    num_ids = len(ids)

    max_matches_for_id = []
    for i in xrange(num_ids-1):
        for j in xrange(i+1, num_ids):
            word_match, num_matches = matches(box_ids[i], box_ids[j])
            # short circuit; initially pursued a more generalized approach
            # in which the max length match would need to be identified
            # and retrieved after running through the entire check
            if num_matches == (len(box_ids[i])-1):
                return word_match

common_letters = match_list(box_ids)
print common_letters
