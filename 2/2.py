#!/usr/bin/env python3

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

import copy

def product_except(a):
    p = 1
    for i in a: p *= i
    for i in range(len(a)): a[i] = p / a[i]
    return a


def test_product_except():
    assert product_except([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_except([3, 2, 1]) == [2, 3, 6]
    assert product_except([2, 2, 3, 4, 5]) == [120, 120, 80, 60, 48]

def product_except_no_divide(a):
    l = copy.deepcopy(a) # cumulative product from left
    r = copy.deepcopy(a) # cumulative product from right

    for i in range(len(a)): # from left to right
        if i != 0:
            l[i] *= l[i-1] # multiply existing value by one to left
    
    for i in range(len(a) -1, -1, -1): # from right to left
        if i != len(a) - 1:
            r[i] *= r[i + 1] # multiply existing value by one to right
    
    # print('left\t', l)
    # print('right\t', r)

    for i in range(len(a)):
        # at first index, solution is second-to-first in index that started at the right
        # this is because it's a cumulative product including all but this index
        if i == 0: a[i] = r[1]

        # at last index, solution is second-to-last in index that started at the left
        # again we see this is a cumulative product including all but this index
        elif i == len(a) - 1: a[i] = l[-2]
        
        # at all other indices, we multiply the cumulative products before/after
        # this works because they are the cumulative products from opposite sides
        # and therefore of all values; because we go from 1 before to 1 after,
        # we know that all values except the current index are included in the product
        else:
            a[i] = l[i - 1] * r [i + 1]
    return a

# print('soln\t', product_except_no_divide([2, 3, 4, 5, 6]))

def test_product_except_no_divide():
    assert product_except_no_divide([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_except_no_divide([3, 2, 1]) == [2, 3, 6]
    assert product_except_no_divide([2, 2, 3, 4, 5]) == [120, 120, 80, 60, 48]