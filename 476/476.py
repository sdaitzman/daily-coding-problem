#!/usr/bin/env python

def find_duplicates(arr):
    d = {}
    dupes = []
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] > 1:
            dupes.append(i)
    return dupes

def test_duplicates():
    assert find_duplicates([1, 2, 3, 3]) == [3]
    assert find_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []
    assert find_duplicates([1, 1, 1, 1]) == [1]
    assert find_duplicates([1, 2, 2, 3, 4, 7]) == [2]
    assert find_duplicates([1, 1, 2, 2, 3, 4, 4, 8, 3, 2, 11, 7, 11]) == [1, 2, 3, 4, 11]
    