#!/usr/bin/env python3

# To test this file, please run `pytest 1.py`


# Naive approach: consider all combinations
# O(n ^ 2), even with the optimization cutting ~half the steps
def is_sum(n, k):
    for i in range(len(n)):
        for j in range(len(n) - i):
            if i != j and n[i] + n[j] == k: return True
    return False

def test_naive():
    assert is_sum([10, 15, 3, 7], 17)
    assert not is_sum([1, 2, 3, 4, 5, 6, 7], 1)
    assert not is_sum([1, 2, 3, 4, 5, 6, 7], 2)
    assert is_sum([1, 2, 3, 4, 5, 6, 7], 3)

# Dict approach
# O(n)
def is_sum_dict(n, k):
    solns = {}
    for i in n:
        if i in solns: return True
        solns[k - i] = True
    return False

def test_dict():
    assert is_sum_dict([10, 15, 3, 7], 17)
    assert not is_sum_dict([1, 2, 3, 4, 5, 6, 7], 1)
    assert not is_sum_dict([1, 2, 3, 4, 5, 6, 7], 2)
    assert is_sum_dict([1, 2, 3, 4, 5, 6, 7], 3)

# Sets approach
# O(n)
def is_sum_sets(n, k):
    solns = set()
    for i in n:
        if i in solns: return True
        solns.add(k - i)
    return False

def test_set():
    assert is_sum_sets([10, 15, 3, 7], 17)
    assert not is_sum_sets([1, 2, 3, 4, 5, 6, 7], 1)
    assert not is_sum_sets([1, 2, 3, 4, 5, 6, 7], 2)
    assert is_sum_sets([1, 2, 3, 4, 5, 6, 7], 3)