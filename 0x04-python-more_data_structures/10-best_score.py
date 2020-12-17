#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        r = sorted(a_dictionary.items())
        r.reverse()
        return r[0][0]
