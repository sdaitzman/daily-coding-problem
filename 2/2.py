#!/usr/bin/env python3

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def product_except(a):
    p = 1
    for i in a: p *= i
    for i in range(len(a)): a[i] = p / a[i]
    return a


def test_product_except():
    assert product_except([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_except([3, 2, 1]) == [2, 3, 6]